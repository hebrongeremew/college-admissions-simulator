"""
Main script for the College Admission Simulator.
"""

from student import Student
from simulator import AdmissionSimulator, EXTRACURRICULAR_CATEGORIES, AWARD_LEVELS
from college_data import COLLEGES

def input_demographics():
    """Collect demographic information."""
    print("\n=== Demographic Information ===")
    name = input("Name: ")
    age = int(input("Age: "))
    gender = input("Gender: ")
    state = input("State (if applicable): ")
    country = input("Country: ")
    underrepresented = input("Underrepresented student status (Y/N): ")
    rural_state = input("Rural state student (Y/N): ")
    figli = input("First-gen low-income (FIGLI) status (Y/N): ")
    return name, age, gender, state, country, underrepresented, rural_state, figli

def input_academic():
    """Collect academic information."""
    print("\n=== Academic Information ===")
    gpa = float(input("GPA: "))
    sat = int(input("SAT: "))
    class_rank = float(input("Class Rank/Percentile (0-100): "))
    school_rank = input("School Rank (within state): ")
    course_rigor = int(input("Course Rigor (Number of AP/IB/Honor classes): "))
    intended_major = input("Intended Major/Field of Study: ")
    return gpa, sat, class_rank, school_rank, course_rigor, intended_major

def input_extracurriculars():
    """Collect extracurricular information."""
    print("\n=== Extracurricular Information ===")
    print("Available categories:", ", ".join(EXTRACURRICULAR_CATEGORIES.keys()))
    extracurriculars = []
    i = 1
    while True:
        add_more = input(f"Add extracurricular {i}? (y/n): ").lower()
        if add_more != 'y':
            break
        category = input("Category: ")
        years = int(input("Number of years: "))
        hours = int(input("Hours per week: "))
        extracurriculars.append({'category': category, 'years': years, 'hours_per_week': hours})
        i += 1
    return extracurriculars

def input_awards():
    """Collect award information."""
    print("\n=== Award Information ===")
    print("Award levels: local (1 pt), regional (2 pts), national (3 pts), international (4 pts)")
    awards = []
    i = 1
    while True:
        add_more = input(f"Add award {i}? (y/n): ").lower()
        if add_more != 'y':
            break
        level = input("Level (local/regional/national/international): ")
        awards.append({'level': level})
        i += 1
    return awards

def input_college_specific_factors(college_name):
    """Collect college-specific factors like legacy status."""
    print(f"\n=== {college_name} Specific Factors ===")
    legacy = input("Legacy status (parent/grandparent/sibling attended) (Y/N): ")
    faculty_child = input("Child of faculty/staff (Y/N): ")
    recruited_athlete = input("Recruited athlete (Y/N): ")
    return legacy, faculty_child, recruited_athlete

def interpret_probability(probability):
    """Convert probability to qualitative assessment."""
    if probability >= 0.8:
        return "Excellent chance - Strong candidate!"
    elif probability >= 0.6:
        return "Good chance - Competitive applicant"
    elif probability >= 0.3:
        return "Fair chance - Possible admission with strong fit"
    elif probability >= 0.1:
        return "Low chance - Reach school"
    else:
        return "Very low chance - Significant reach"

def main():
    print("Welcome to the College Admission Simulator!")
    print("==========================================")

    try:
        # Collect general information (not college-specific)
        demo = input_demographics()
        acad = input_academic()
        extra = input_extracurriculars()
        awards = input_awards()

        print("\nAvailable Colleges:")
        for i, college in enumerate(COLLEGES.keys(), 1):
            print(f"{i}. {college}")

        choice = int(input("\nSelect a college by number: "))
        if not 1 <= choice <= len(COLLEGES):
            raise ValueError("Invalid choice.")

        college_name = list(COLLEGES.keys())[choice - 1]

        # Now collect college-specific factors
        misc = input_college_specific_factors(college_name)

        # Create student object
        student = Student(*demo, *acad, extra, awards, *misc)

        simulator = AdmissionSimulator()
        probability = simulator.calculate_probability(student, college_name)

        print(f"\nStudent Profile: {student}")
        print(f"College: {college_name}")
        assessment = interpret_probability(probability)
        print(f"Admission Probability: {probability:.1%}")
        print(f"Assessment: {assessment}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()

if __name__ == "__main__":
    main()