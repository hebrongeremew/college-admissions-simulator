# Import Flask web framework tools and college database with major categorization helper
from flask import Flask, render_template, request, jsonify
from college_data import COLLEGES, get_major_category

# Create Flask application instance to handle web requests and routing
app = Flask(__name__)

# Define base point values for different extracurricular categories to prioritize leadership and research
EXTRACURRICULAR_WEIGHTS = {
    "Leadership": 3, "Academic": 2, "Sports": 3,
    "Music": 2, "Arts": 2, "Volunteering": 2,
    "Research": 3, "Clubs": 1, "Job": 2,
    "Internship": 3
}
# Map display category names to database preference keys for college-specific activity matching
CATEGORY_MAP = {
    "Leadership": "leadership",
    "Academic": "academic",
    "Sports": "sports",
    "Music": "music",
    "Arts": "arts",
    "Volunteering": "volunteering",
    "Research": "research",
    "Clubs": "clubs",
    "Job": "job",
    "Internship": "internship"
}
# Assign point values to award levels, with international awards worth the most
AWARD_WEIGHTS = {
    "local": 1, "regional": 2, "national": 3, "international": 4
}

# Real-world acceptance rate caps per college.
# Even a "perfect" applicant cannot exceed these — they reflect the hard ceiling
# imposed by class size, yield management, and sheer competition.
REALISTIC_MAX_CHANCE = {
    "Harvard University": 65.0,
    "Stanford University": 65.0,
    "MIT": 65.0,
    "Yale University": 65.0,
    "Princeton University": 65.0,
    "Columbia University": 65.0,
    "University of Pennsylvania": 70.0,
    "Brown University": 70.0,
    "Dartmouth College": 70.0,
    "Cornell University": 75.0,
    "University of Chicago": 65.0,
    "Duke University": 70.0,
    "Northwestern University": 70.0,
    "California Institute of Technology": 65.0,
    "Johns Hopkins University": 70.0,
    "Rice University": 75.0,
    "Vanderbilt University": 75.0,
    "University of California, Berkeley": 80.0,
    "University of Michigan": 85.0,
    "University of California, Los Angeles": 80.0,
    "Carnegie Mellon University": 80.0,
    "University of Notre Dame": 80.0,
    "Washington University in St. Louis": 80.0
}

def calculate_admission_chance(student_data, college_name):
    if college_name not in COLLEGES:
        return 50.0

    college = COLLEGES[college_name]
    major_category = get_major_category(student_data.get('major', 'Undecided'))
    weights = college['major_weights'][major_category]

    sat_math = min(max(student_data.get('sat_math', 0), 0), 800)
    sat_rw = min(max(student_data.get('sat_rw', 0), 0), 800)
    act = min(max(student_data.get('act', 0), 0), 36)
    total_sat = sat_math + sat_rw

    sat_math_score = sat_math / 800
    sat_rw_score = sat_rw / 800
    act_score = act / 36

    math_weight = college.get('sat_math_weight', 0.5)
    rw_weight = college.get('sat_rw_weight', 0.5)
    if math_weight + rw_weight <= 0:
        math_weight, rw_weight = 0.5, 0.5

    sat_percentile = sat_math_score * math_weight + sat_rw_score * rw_weight

    exam_mode = None
    if sat_math > 0 or sat_rw > 0:
        exam_mode = 'sat'
    if act > 0 and (exam_mode is None or act_score >= sat_percentile):
        exam_mode = 'act'

    exam_percentile = act_score if exam_mode == 'act' else sat_percentile
    if exam_mode is None:
        exam_percentile = 0.10  # No scores = very weak signal for selective schools

    raw_avg_sat = college.get('avg_sat')

    if raw_avg_sat is None:
        raw_avg_sat = college.get('avg_sat_math', 0) + college.get('avg_sat_rw', 0)
    
    if raw_avg_sat > 0:
        avg_sat = raw_avg_sat
    else:
        avg_sat = None  # test-blind / no SAT data

    if avg_sat and exam_mode == 'sat':
        exam_quality = 1 - max(0.0, min(1.0, (avg_sat - total_sat) / 400))
    elif avg_sat and exam_mode == 'act':
        avg_act_equivalent = avg_sat / 1600 * 36
        exam_quality = 1 - max(0.0, min(1.0, (avg_act_equivalent - act) / 10))
    else:
        exam_quality = 1.0

    # Stricter score penalty thresholds than before
    if exam_mode == 'sat':
        exam_penalty = 1.0
        if sat_math_score < 0.50 and math_weight >= 0.4:
            exam_penalty -= 0.20
        if sat_rw_score < 0.50 and rw_weight >= 0.4:
            exam_penalty -= 0.20
        exam_penalty = max(0.55, exam_penalty)
        exam_percentile *= exam_penalty

    gpa_percentile = min(max(student_data['gpa'], 0.0), 4.0) / 4.0
    rank_percentile = min(max(student_data['class_rank'], 0), 100) / 100
    rigor_score = min(max(student_data['rigor'], 1), 10) / 10

    academic_score = (
        exam_percentile * 0.42 +
        gpa_percentile * 0.33 +
        rank_percentile * 0.15 +
        rigor_score * 0.10
    )
    academic_score *= 0.65 + exam_quality * 0.35

    # Aggressive diminishing returns — a perfect profile still isn't a lock
    if academic_score > 0.75:
        academic_score = 0.75 + (academic_score - 0.75) * 0.25

    academic_score = max(0.0, min(0.85, academic_score))

    # Multi-flag academic penalty system — being below average on several dimensions
    # compounds badly, as it does in real admissions
    low_academic_flags = 0
    if exam_mode == 'sat' and avg_sat:
        if total_sat < avg_sat * 0.92:
            low_academic_flags += 1
        if total_sat < avg_sat * 0.85:
            low_academic_flags += 1  # Double-hit for being far below avg
        if sat_math_score < 0.50:
            low_academic_flags += 1
        if sat_rw_score < 0.50:
            low_academic_flags += 1
    elif exam_mode == 'act' and avg_sat:
        avg_act_equivalent = avg_sat / 1600 * 36
        if act < avg_act_equivalent * 0.92:
            low_academic_flags += 1
        if act < avg_act_equivalent * 0.85:
            low_academic_flags += 1
    else:
        low_academic_flags += 3

    avg_gpa = college.get('avg_gpa', 3.0)
    if student_data['gpa'] < avg_gpa * 0.97:
        low_academic_flags += 1
    if student_data['gpa'] < avg_gpa * 0.92:
        low_academic_flags += 1  # Extra hit for being significantly below avg GPA
    if student_data['class_rank'] < 75:
        low_academic_flags += 1
    if student_data['class_rank'] < 50:
        low_academic_flags += 1

    if low_academic_flags >= 4:
        academic_score *= 0.30
    elif low_academic_flags == 3:
        academic_score *= 0.45
    elif low_academic_flags == 2:
        academic_score *= 0.62
    elif low_academic_flags == 1:
        academic_score *= 0.80

    extracurricular_score = 0
    for activity in student_data['extracurriculars']:
        if activity.get('years') and activity.get('hours'):
            base_weight = EXTRACURRICULAR_WEIGHTS.get(activity['category'], 1)
            mapped_category = CATEGORY_MAP.get(activity['category'], "").lower()
            pref_multiplier = college.get('preferences', {}).get(mapped_category, 1)
            category_weight = base_weight * pref_multiplier
            years_factor = min(activity['years'] / 4, 1)
            hours_factor = min(activity['hours'] / 20, 1)
            extracurricular_score += category_weight * (years_factor + hours_factor) / 2
    extracurricular_score = min(extracurricular_score / 14, 1)  # Hard to max out

    awards_score = 0
    for award in student_data['awards']:
        awards_score += AWARD_WEIGHTS.get(award['level'], 1)
    awards_score = min(awards_score / 14, 1)  # Hard to max out

    spike_score = 0

    # Awards spike
    high_awards = sum(1 for a in student_data['awards'] if a.get('level') in ['national', 'international'])
    
    if any(a.get('level') == 'international' for a in student_data['awards']):
        spike_score += 1
    elif high_awards >= 2:
        spike_score += 1

    # Extracurricular spike
    for ec in student_data['extracurriculars']:
        if ec.get('years', 0) >= 3 and ec.get('hours', 0) >= 10:
            spike_score += 1
            break

    total_weight = max(
        1,
        weights.get('academic_weight', 1) +
        weights.get('activity_weight', 1) +
        weights.get('misc_weight', 1)
    )
    base_chance = (
        academic_score * weights['academic_weight'] +
        extracurricular_score * weights['activity_weight'] +
        awards_score * weights['misc_weight']
    ) / total_weight

    # Consider potential spikes 
    if spike_score >= 1:
        base_chance *= 1.15
    if spike_score >= 2:
        base_chance *= 1.25
    # Academic gate: penalize applicants below the school's academic profile
    raw_avg_sat = college.get('avg_sat')

    if raw_avg_sat is None:
        raw_avg_sat = college.get('avg_sat_math', 0) + college.get('avg_sat_rw', 0)
    
    avg_sat = raw_avg_sat if raw_avg_sat > 0 else None
    avg_gpa = college.get("avg_gpa", 3.0)
    
    if avg_sat and total_sat > 0:
        sat_ratio = total_sat / avg_sat
    else:
        sat_ratio = 1.0  # no SAT penalty for test-blind/test-free schools
    
    gpa_ratio = student_data["gpa"] / avg_gpa if avg_gpa > 0 else 0
    
    academic_gate = 1.0
    
    # SAT penalties
    if sat_ratio < 0.85:
        academic_gate *= 0.20
    elif sat_ratio < 0.90:
        academic_gate *= 0.35
    elif sat_ratio < 0.95:
        academic_gate *= 0.60
    elif sat_ratio < 0.98:
        academic_gate *= 0.80
    
    # GPA penalties
    if gpa_ratio < 0.80:
        academic_gate *= 0.15
    elif gpa_ratio < 0.85:
        academic_gate *= 0.25
    elif gpa_ratio < 0.90:
        academic_gate *= 0.40
    elif gpa_ratio < 0.95:
        academic_gate *= 0.65
    elif gpa_ratio < 0.98:
        academic_gate *= 0.80
    
    base_chance *= academic_gate

    if academic_score < 0.30:
        base_chance *= 0.35
    elif academic_score < 0.45:
        base_chance *= 0.60
    
    # Convert the college's selectivity into a baseline acceptance percentage
    selectivity = college.get("selectivity", 0.10)
    baseline_chance = selectivity * 100
    
    # Stronger applicants rise above the baseline rate
    strength_multiplier = 1 + (base_chance * 2.5)
    
    final_chance = baseline_chance * strength_multiplier

    # Background factor boosts
    background_boost = 1.0
    if student_data.get('legacy'):
        background_boost += 0.08
    if student_data.get('first_gen'):
        background_boost += 0.04
    if student_data.get('underrepresented'):
        background_boost += 0.05
    if student_data.get('athlete'):
        background_boost += 0.10
    if student_data.get('faculty_child'):
        background_boost += 0.06

    final_chance *= background_boost

    # Hard cap: no one exceeds the realistic maximum for this school
    max_chance = REALISTIC_MAX_CHANCE.get(college_name, 60.0)
    final_chance = min(final_chance, max_chance)

    return round(max(1, final_chance), 1)
    
def strength_priority(s): # Orders strenghts by importance 
    s = s.lower()

    if "recruited athlete" in s:
        return 0
    elif "spike" in s or "international" in s or "national level" in s:
        return 1
    elif "gpa" in s or "class rank" in s or "rigor" in s:
        return 2
    elif "sat" in s or "act" in s:
        return 3
    elif "first-generation" in s or "underrepresented" in s or "legacy" in s or "faculty" in s:
        return 4
    elif "extracurricular profile" in s or "award record" in s:
        return 5
    else:
        return 6
        


def weakness_priority(w): 
    w = w.lower()

    if "gpa" in w or "sat" in w or "act" in w or "class rank" in w:
        return 0

    elif "rigor" in w:
        return 1

    elif "extracurricular" in w:
        return 2

    elif "award" in w:
        return 3
        
    else:
        return 4



def identify_strengths_weaknesses(student_data, college_name):
    college = COLLEGES.get(college_name, {})
    strengths = []
    weaknesses = []

    if college:
        sat_math = student_data.get('sat_math', 0)
        sat_rw = student_data.get('sat_rw', 0)
        act = student_data.get('act', 0)
        total_sat = sat_math + sat_rw
        
        raw_avg_sat = college.get('avg_sat')

        if raw_avg_sat is None:
            raw_avg_sat = college.get('avg_sat_math', 0) + college.get('avg_sat_rw', 0)
        
        if raw_avg_sat > 0:
            avg_sat = raw_avg_sat
        else:
            avg_sat = None

        if act > 0 and avg_sat:
            avg_act_equivalent = avg_sat / 1600 * 36
            if act >= avg_act_equivalent:
                strengths.append(f"ACT score ({act}) meets or exceeds {college_name}'s average equivalent ({avg_act_equivalent:.0f})")
            else:
                weaknesses.append(f"ACT score ({act}) is below {college_name}'s average equivalent ({avg_act_equivalent:.0f})")
        elif total_sat > 0 and avg_sat:
            if total_sat >= avg_sat:
                strengths.append(f"SAT total ({total_sat}) meets or exceeds {college_name} average ({avg_sat})")
            else:
                weaknesses.append(f"SAT total ({total_sat}) is below {college_name} average ({avg_sat})")

        if sat_math > 0 and avg_sat:
            if sat_math < 600:
                weaknesses.append("SAT Math is below the competitive range for selective schools")
            elif sat_math < 700:
                weaknesses.append(f"SAT Math ({sat_math}) is decent, but below the typical range for many top schools")
            elif sat_math >= 750:
                strengths.append(f"SAT Math ({sat_math}) is exceptionally strong")
            else:
                strengths.append(f"SAT Math ({sat_math}) is competitive")

        if sat_rw > 0 and avg_sat:
            if sat_rw < 600:
                weaknesses.append("SAT Reading/Writing is below the competitive range for selective schools")
            elif sat_rw < 700:
                weaknesses.append(f"SAT Reading/Writing ({sat_rw}) is decent, but below the typical range for many top schools")
            elif sat_rw >= 740:
                strengths.append(f"SAT Reading/Writing ({sat_rw}) is exceptionally strong")
            else:
                strengths.append(f"SAT Reading/Writing ({sat_rw}) is competitive")

        if act > 0 and act < 28:
            weaknesses.append(f"ACT composite ({act}) is below the typical range for this school")

        avg_gpa = college.get('avg_gpa', 3.0)
        if student_data['gpa'] >= avg_gpa:
            strengths.append(f"GPA ({student_data['gpa']}) meets or exceeds {college_name} average ({avg_gpa})")
        else:
            weaknesses.append(f"GPA ({student_data['gpa']}) is below {college_name} average ({avg_gpa})")

    if len(student_data['extracurriculars']) >= 4:
        strengths.append(f"Strong extracurricular profile ({len(student_data['extracurriculars'])} activities)")
    elif len(student_data['extracurriculars']) <= 1:
        weaknesses.append("Thin extracurricular profile — top schools expect depth and sustained commitment")

    if len(student_data['awards']) >= 3:
        strengths.append(f"Impressive award record ({len(student_data['awards'])} honors)")
    elif len(student_data['awards']) == 0:
        weaknesses.append("No awards listed — competitive applicants typically have notable recognition")

    rank = int(student_data['class_rank'])

    if rank == 99:
        strengths.append("Exceptional class rank (top 1%)")
    elif rank == 95:
        strengths.append("Outstanding class rank (top 5%)")
    elif rank == 90:
        strengths.append("Strong class rank (top 10%)")
    elif rank == 75:
        strengths.append("Above-average class rank (top 25%)")
    elif rank == 50:
        weaknesses.append("Class rank (bottom 50%) may be a concern for highly selective schools")

    if student_data['rigor'] >= 9:
        strengths.append("Exceptionally rigorous course load (multiple AP/IB courses)")
    elif student_data['rigor'] >= 7:
        strengths.append("Strong course rigor")
    elif student_data['rigor'] <= 4:
        weaknesses.append("Course rigor is low — selective schools expect the most challenging available curriculum")

    # Misc. factors
    if student_data.get('legacy'):
        strengths.append("Legacy status provides a modest admissions advantage")
    if student_data.get('athlete'):
        strengths.append("Recruited athlete status is one of the strongest hooks available")
    if student_data.get('first_gen'):
        strengths.append("First-generation college student status is valued for diversity")
    if student_data.get('underrepresented'):
        strengths.append("Underrepresented minority status contributes to institutional diversity goals")
    if student_data.get('faculty_child'):
        strengths.append("Child of faculty/staff may receive preferential consideration")
   
    # Spike factors
    high_awards = sum(
        1 for a in student_data['awards']
        if a.get('level') in ['national', 'international']
    )
    
    if any(a.get('level') == 'international' for a in student_data['awards']):
        strengths.append("Exceptional achievement: international-level recognition (spike)")
    elif high_awards >= 2:
        strengths.append("Strong award profile at a national level (spike)")

    for ec in student_data['extracurriculars']:
        if ec.get('years', 0) >= 3 and ec.get('hours', 0) >= 10:
            strengths.append("Deep extracurricular commitment shows a strong spike in involvement")
            break
    
    strengths.sort(key=strength_priority)
    weaknesses.sort(key=weakness_priority)

    return strengths, weaknesses


    

@app.route('/')
def index():
    return render_template('index.html', colleges=list(COLLEGES.keys()))


@app.route('/evaluate', methods=['POST'])
def evaluate():
    try:
        data = request.get_json()
        student_data = {
            'sat_math': data.get('sat_math', 0),
            'sat_rw': data.get('sat_rw', 0),
            'act': data.get('act', 0),
            'gpa': data.get('gpa', 3.0),
            'class_rank': data.get('class_rank', 50),
            'rigor': data.get('rigor', 5),
            'major': data.get('major', 'Undecided'),
            'legacy': data.get('legacy', False),
            'first_gen': data.get('first_gen', False),
            'underrepresented': data.get('underrepresented', False),
            'athlete': data.get('athlete', False),
            'faculty_child': data.get('faculty_child', False),
            'extracurriculars': data.get('extracurriculars', []),
            'awards': data.get('awards', [])
        }

        selected_colleges = data.get('colleges', [])
        if not selected_colleges:
            return jsonify({'error': 'No colleges selected'}), 400

        results = []
        for college in selected_colleges:
            chance = calculate_admission_chance(student_data, college)
            strengths, weaknesses = identify_strengths_weaknesses(student_data, college)
            results.append({
                'college': college,
                'chance': chance,
                'strengths': strengths[:5],
                'weaknesses': weaknesses[:5]
            })

        results.sort(key=lambda x: x['chance'], reverse=True)
        return jsonify(results)

    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5000)

