from flask import Flask, render_template, request, jsonify
from college_data import COLLEGES, get_major_category

app = Flask(__name__)

EXTRACURRICULAR_WEIGHTS = {
    "Leadership": 3, "Academic": 2, "Sports": 3,
    "Music": 2, "Arts": 2, "Volunteering": 2,
    "Research": 3, "Clubs": 1
}

AWARD_WEIGHTS = {
    "local": 1, "regional": 2, "national": 3, "international": 4
}

def calculate_admission_chance(student_data, college_name):
    if college_name not in COLLEGES:
        return 50.0

    college = COLLEGES[college_name]
    major_category = get_major_category(student_data.get('major', 'Undecided'))
    weights = college['major_weights'][major_category]

    sat_percentile = (student_data['sat'] - 400) / 1200
    gpa_percentile = student_data['gpa'] / 4.0
    rank_percentile = student_data['class_rank'] / 100
    rigor_score = student_data['rigor'] / 10

    academic_score = (sat_percentile * 0.35 + gpa_percentile * 0.35 +
                      rank_percentile * 0.15 + rigor_score * 0.15)

    sat_competitive = 1 - max(0, min(1, (college['avg_sat'] - student_data['sat']) / 400))
    gpa_competitive = 1 - max(0, min(1, (college['avg_gpa'] - student_data['gpa']) / 1.0))
    academic_final = academic_score * 0.6 + sat_competitive * 0.2 + gpa_competitive * 0.2

    extracurricular_score = 0
    for activity in student_data['extracurriculars']:
        if activity.get('years') and activity.get('hours'):
            category_weight = EXTRACURRICULAR_WEIGHTS.get(activity['category'], 1)
            years_factor = min(activity['years'] / 4, 1)
            hours_factor = min(activity['hours'] / 20, 1)
            extracurricular_score += category_weight * (years_factor + hours_factor) / 2
    extracurricular_score = min(extracurricular_score / 10, 1)

    awards_score = 0
    for award in student_data['awards']:
        awards_score += AWARD_WEIGHTS.get(award['level'], 1)
    awards_score = min(awards_score / 10, 1)

    base_chance = (academic_final * weights['academic_weight'] +
                   extracurricular_score * weights['activity_weight'] +
                   awards_score * weights['misc_weight'])

    final_chance = base_chance * 100 * (1 - college['selectivity'])
    return round(max(5, min(95, final_chance)), 1)


def identify_strengths_weaknesses(student_data, college_name):
    college = COLLEGES.get(college_name, {})
    strengths = []
    weaknesses = []

    if college:
        if student_data['sat'] >= college['avg_sat']:
            strengths.append(f"SAT score ({student_data['sat']}) above {college_name} average ({college['avg_sat']})")
        else:
            weaknesses.append(f"SAT score ({student_data['sat']}) below {college_name} average ({college['avg_sat']})")

        if student_data['gpa'] >= college['avg_gpa']:
            strengths.append(f"GPA ({student_data['gpa']}) above {college_name} average ({college['avg_gpa']})")
        else:
            weaknesses.append(f"GPA ({student_data['gpa']}) below {college_name} average ({college['avg_gpa']})")

    if len(student_data['extracurriculars']) >= 3:
        strengths.append(f"Strong extracurricular involvement ({len(student_data['extracurriculars'])} activities)")
    elif len(student_data['extracurriculars']) == 0:
        weaknesses.append("No extracurricular activities listed")

    if len(student_data['awards']) >= 2:
        strengths.append(f"Notable awards and honors ({len(student_data['awards'])} awards)")
    elif len(student_data['awards']) == 0:
        weaknesses.append("No awards or honors listed")

    if student_data['class_rank'] >= 90:
        strengths.append(f"Excellent class rank (top {100 - student_data['class_rank']}%)")
    elif student_data['class_rank'] < 50:
        weaknesses.append(f"Class rank could be improved (top {100 - student_data['class_rank']}%)")

    if student_data['rigor'] >= 8:
        strengths.append("Very rigorous course load")
    elif student_data['rigor'] <= 4:
        weaknesses.append("Course rigor could be increased")

    return strengths, weaknesses


@app.route('/')
def index():
    return render_template('index.html', colleges=list(COLLEGES.keys()))


@app.route('/evaluate', methods=['POST'])
def evaluate():
    try:
        data = request.get_json()

        student_data = {
            'sat': data.get('sat', 1200),
            'gpa': data.get('gpa', 3.0),
            'class_rank': data.get('class_rank', 50),
            'rigor': data.get('rigor', 5),
            'major': data.get('major', 'Undecided'),
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