"""
Test script for the College Admission Simulator.
"""

from student import Student
from simulator import AdmissionSimulator

def test_simulator():
    # Create a sample student with comprehensive profile
    student = Student(
        name="John Doe",
        age=18,
        gender="Male",
        state="California",
        country="USA",
        underrepresented="Y",
        rural_state="N",
        figli="Y",
        gpa=3.8,
        sat_score=1500,
        class_rank_percentile=95,
        school_rank="Top 10 in state",
        course_rigor=8,
        intended_major="Computer Science",
        extracurriculars=[
            {'category': 'Sports', 'years': 3, 'hours_per_week': 15},
            {'category': 'Leadership', 'years': 2, 'hours_per_week': 10}
        ],
        awards=[
            {'level': 'national'},
            {'level': 'regional'}
        ],
        legacy="N",
        faculty_child="N",
        recruited_athlete="N"
    )

    # Create simulator
    sim = AdmissionSimulator()

    # Test with MIT for different majors
    student.intended_major = "Computer Science"
    prob_stem = sim.calculate_probability(student, "MIT")
    print(f"MIT Probability for Computer Science major: {prob_stem:.2%}")

    student.intended_major = "English"
    prob_humanities = sim.calculate_probability(student, "MIT")
    print(f"MIT Probability for English major: {prob_humanities:.2%}")

    student.intended_major = "Fine Arts"
    prob_arts = sim.calculate_probability(student, "MIT")
    print(f"MIT Probability for Fine Arts major: {prob_arts:.2%}")

    # Test with Yale for comparison
    student.intended_major = "Fine Arts"
    prob_yale_arts = sim.calculate_probability(student, "Yale University")
    print(f"Yale Probability for Fine Arts major: {prob_yale_arts:.2%}")

    print("Test completed successfully!")

if __name__ == "__main__":
    test_simulator()