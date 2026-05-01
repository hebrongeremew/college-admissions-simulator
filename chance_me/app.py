# Import Flask web framework tools and college database with major categorization helper
from flask import Flask, render_template, request, jsonify
from college_data import COLLEGES, get_major_category

# Create Flask application instance to handle web requests and routing
app = Flask(__name__)

# Define base point values for different extracurricular categories to prioritize leadership and research
EXTRACURRICULAR_WEIGHTS = {
    "Leadership": 3, "Academic": 2, "Sports": 3,
    "Music": 2, "Arts": 2, "Volunteering": 2,
    "Research": 3, "Clubs": 1
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
    "Clubs": "clubs"
}
# Assign point values to award levels, with international awards worth the most
AWARD_WEIGHTS = {
    "local": 1, "regional": 2, "national": 3, "international": 4
}

# Real-world acceptance rate caps per college.
# Even a "perfect" applicant cannot exceed these — they reflect the hard ceiling
# imposed by class size, yield management, and sheer competition.
REALISTIC_MAX_CHANCE = {
    "Harvard University":                 12.0,
    "Stanford University":                10.0,
    "MIT":                                14.0,
    "Yale University":                    12.0,
    "Princeton University":               11.0,
    "Columbia University":                11.0,
    "University of Pennsylvania":         16.0,
    "Brown University":                   16.0,
    "Dartmouth College":                  15.0,
    "Cornell University":                 22.0,
    "University of California, Berkeley": 40.0,
    "University of Michigan":             45.0,
    "University of Virginia":             50.0,
}

# How harshly selectivity compresses scores for elite schools.
# Higher = more brutal compression even for strong applicants.
SELECTIVITY_COMPRESSION = {
    "Harvard University":                 0.970,
    "Stanford University":                0.972,
    "MIT":                                0.965,
    "Yale University":                    0.970,
    "Princeton University":               0.970,
    "Columbia University":                0.970,
    "University of Pennsylvania":         0.960,
    "Brown University":                   0.960,
    "Dartmouth College":                  0.962,
    "Cornell University":                 0.940,
    "University of California, Berkeley": 0.880,
    "University of Michigan":             0.850,
    "University of Virginia":             0.830,
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

    avg_sat = college.get('avg_sat', 1200)

    if exam_mode == 'sat':
        exam_quality = 1 - max(0.0, min(1.0, (avg_sat - total_sat) / 400))
    else:
        avg_act_equivalent = avg_sat / 1600 * 36
        exam_quality = 1 - max(0.0, min(1.0, (avg_act_equivalent - act) / 10))

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
    if exam_mode == 'sat':
        if total_sat < avg_sat * 0.92:
            low_academic_flags += 1
        if total_sat < avg_sat * 0.85:
            low_academic_flags += 1  # Double-hit for being far below avg
        if sat_math_score < 0.50:
            low_academic_flags += 1
        if sat_rw_score < 0.50:
            low_academic_flags += 1
    elif exam_mode == 'act':
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

    # Apply college-specific selectivity compression
    compression = SELECTIVITY_COMPRESSION.get(college_name, 0.90)
    final_chance = base_chance * 100 * (1 - compression)

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


def identify_strengths_weaknesses(student_data, college_name):
    college = COLLEGES.get(college_name, {})
    strengths = []
    weaknesses = []

    if college:
        sat_math = student_data.get('sat_math', 0)
        sat_rw = student_data.get('sat_rw', 0)
        act = student_data.get('act', 0)
        total_sat = sat_math + sat_rw
        avg_sat = college.get('avg_sat', 1200)

        if act > 0:
            avg_act_equivalent = avg_sat / 1600 * 36
            if act >= avg_act_equivalent:
                strengths.append(f"ACT score ({act}) meets or exceeds {college_name}'s average equivalent ({avg_act_equivalent:.0f})")
            else:
                weaknesses.append(f"ACT score ({act}) is below {college_name}'s average equivalent ({avg_act_equivalent:.0f})")
        elif total_sat > 0:
            if total_sat >= avg_sat:
                strengths.append(f"SAT total ({total_sat}) meets or exceeds {college_name} average ({avg_sat})")
            else:
                weaknesses.append(f"SAT total ({total_sat}) is below {college_name} average ({avg_sat})")

        if sat_math > 0:
            if sat_math < 500:
                weaknesses.append("SAT Math is below the competitive threshold for selective programs")
            elif sat_math >= 750:
                strengths.append(f"SAT Math ({sat_math}) is exceptionally strong")
            else:
                strengths.append(f"SAT Math ({sat_math}) is competitive")

        if sat_rw > 0:
            if sat_rw < 500:
                weaknesses.append("SAT Reading/Writing is below the competitive threshold for selective programs")
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

    if student_data['class_rank'] >= 95:
        strengths.append(f"Outstanding class rank (top {100 - student_data['class_rank']}%)")
    elif student_data['class_rank'] >= 85:
        strengths.append(f"Strong class rank (top {100 - student_data['class_rank']}%)")
    elif student_data['class_rank'] < 75:
        weaknesses.append(f"Class rank (top {100 - student_data['class_rank']}%) is below what most selective schools expect")

    if student_data['rigor'] >= 9:
        strengths.append("Exceptionally rigorous course load (multiple AP/IB courses)")
    elif student_data['rigor'] >= 7:
        strengths.append("Strong course rigor")
    elif student_data['rigor'] <= 4:
        weaknesses.append("Course rigor is low — selective schools expect the most challenging available curriculum")

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
                'strengths': strengths[:3],
                'weaknesses': weaknesses[:3]
            })

        results.sort(key=lambda x: x['chance'], reverse=True)
        return jsonify(results)

    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5000)