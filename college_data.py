"""
College data module containing information about various colleges.
"""

"""
College data module containing information about various colleges.
"""

# Major categories and their typical focus areas
MAJOR_CATEGORIES = {
    "STEM": ["Computer Science", "Engineering", "Mathematics", "Physics", "Chemistry", "Biology"],
    "Humanities": ["English", "History", "Philosophy", "Languages", "Classics"],
    "Social Sciences": ["Psychology", "Economics", "Political Science", "Sociology", "Anthropology"],
    "Arts": ["Fine Arts", "Music", "Theater", "Film", "Design"],
    "Business": ["Business", "Finance", "Marketing", "Management"],
    "Pre-Med/Health": ["Pre-Med", "Nursing", "Public Health", "Biochemistry"],
    "Undecided": ["Undecided", "Exploring Options"]
}

def get_major_category(intended_major):
    """Determine the major category for a given intended major."""
    for category, majors in MAJOR_CATEGORIES.items():
        if any(major.lower() in intended_major.lower() for major in majors):
            return category
    return "Undecided"  # Default category

COLLEGES = {
    "Harvard University": {
        "avg_sat": 1520,
        "avg_gpa": 4.0,
        "selectivity": 0.05,  # 5% acceptance rate
        "major_weights": {
            "STEM": {"academic_weight": 0.6, "activity_weight": 0.25, "misc_weight": 0.15},
            "Humanities": {"academic_weight": 0.45, "activity_weight": 0.35, "misc_weight": 0.2},
            "Social Sciences": {"academic_weight": 0.5, "activity_weight": 0.3, "misc_weight": 0.2},
            "Arts": {"academic_weight": 0.4, "activity_weight": 0.4, "misc_weight": 0.2},
            "Business": {"academic_weight": 0.55, "activity_weight": 0.3, "misc_weight": 0.15},
            "Pre-Med/Health": {"academic_weight": 0.6, "activity_weight": 0.25, "misc_weight": 0.15},
            "Undecided": {"academic_weight": 0.5, "activity_weight": 0.3, "misc_weight": 0.2}
        }
    },
    "Stanford University": {
        "avg_sat": 1500,
        "avg_gpa": 3.96,
        "selectivity": 0.04,
        "major_weights": {
            "STEM": {"academic_weight": 0.65, "activity_weight": 0.2, "misc_weight": 0.15},
            "Humanities": {"academic_weight": 0.45, "activity_weight": 0.35, "misc_weight": 0.2},
            "Social Sciences": {"academic_weight": 0.5, "activity_weight": 0.3, "misc_weight": 0.2},
            "Arts": {"academic_weight": 0.4, "activity_weight": 0.4, "misc_weight": 0.2},
            "Business": {"academic_weight": 0.55, "activity_weight": 0.3, "misc_weight": 0.15},
            "Pre-Med/Health": {"academic_weight": 0.6, "activity_weight": 0.25, "misc_weight": 0.15},
            "Undecided": {"academic_weight": 0.5, "activity_weight": 0.3, "misc_weight": 0.2}
        }
    },
    "MIT": {
        "avg_sat": 1540,
        "avg_gpa": 4.17,
        "selectivity": 0.07,
        "major_weights": {
            "STEM": {"academic_weight": 0.7, "activity_weight": 0.15, "misc_weight": 0.15},
            "Humanities": {"academic_weight": 0.5, "activity_weight": 0.3, "misc_weight": 0.2},
            "Social Sciences": {"academic_weight": 0.55, "activity_weight": 0.25, "misc_weight": 0.2},
            "Arts": {"academic_weight": 0.45, "activity_weight": 0.35, "misc_weight": 0.2},
            "Business": {"academic_weight": 0.6, "activity_weight": 0.25, "misc_weight": 0.15},
            "Pre-Med/Health": {"academic_weight": 0.65, "activity_weight": 0.2, "misc_weight": 0.15},
            "Undecided": {"academic_weight": 0.55, "activity_weight": 0.25, "misc_weight": 0.2}
        }
    },
    "Yale University": {
        "avg_sat": 1510,
        "avg_gpa": 4.0,
        "selectivity": 0.06,
        "major_weights": {
            "STEM": {"academic_weight": 0.55, "activity_weight": 0.3, "misc_weight": 0.15},
            "Humanities": {"academic_weight": 0.4, "activity_weight": 0.4, "misc_weight": 0.2},
            "Social Sciences": {"academic_weight": 0.45, "activity_weight": 0.35, "misc_weight": 0.2},
            "Arts": {"academic_weight": 0.35, "activity_weight": 0.45, "misc_weight": 0.2},
            "Business": {"academic_weight": 0.5, "activity_weight": 0.3, "misc_weight": 0.2},
            "Pre-Med/Health": {"academic_weight": 0.55, "activity_weight": 0.3, "misc_weight": 0.15},
            "Undecided": {"academic_weight": 0.45, "activity_weight": 0.35, "misc_weight": 0.2}
        }
    },
    "Princeton University": {
        "avg_sat": 1500,
        "avg_gpa": 3.9,
        "selectivity": 0.06,
        "major_weights": {
            "STEM": {"academic_weight": 0.6, "activity_weight": 0.25, "misc_weight": 0.15},
            "Humanities": {"academic_weight": 0.45, "activity_weight": 0.35, "misc_weight": 0.2},
            "Social Sciences": {"academic_weight": 0.5, "activity_weight": 0.3, "misc_weight": 0.2},
            "Arts": {"academic_weight": 0.4, "activity_weight": 0.4, "misc_weight": 0.2},
            "Business": {"academic_weight": 0.55, "activity_weight": 0.3, "misc_weight": 0.15},
            "Pre-Med/Health": {"academic_weight": 0.6, "activity_weight": 0.25, "misc_weight": 0.15},
            "Undecided": {"academic_weight": 0.5, "activity_weight": 0.3, "misc_weight": 0.2}
        }
    },
    "University of California, Berkeley": {
        "avg_sat": 1420,
        "avg_gpa": 3.89,
        "selectivity": 0.15,
        "major_weights": {
            "STEM": {"academic_weight": 0.65, "activity_weight": 0.2, "misc_weight": 0.15},
            "Humanities": {"academic_weight": 0.5, "activity_weight": 0.3, "misc_weight": 0.2},
            "Social Sciences": {"academic_weight": 0.55, "activity_weight": 0.25, "misc_weight": 0.2},
            "Arts": {"academic_weight": 0.45, "activity_weight": 0.35, "misc_weight": 0.2},
            "Business": {"academic_weight": 0.6, "activity_weight": 0.25, "misc_weight": 0.15},
            "Pre-Med/Health": {"academic_weight": 0.65, "activity_weight": 0.2, "misc_weight": 0.15},
            "Undecided": {"academic_weight": 0.55, "activity_weight": 0.25, "misc_weight": 0.2}
        }
    },
    "University of Michigan": {
        "avg_sat": 1430,
        "avg_gpa": 3.87,
        "selectivity": 0.23,
        "major_weights": {
            "STEM": {"academic_weight": 0.6, "activity_weight": 0.25, "misc_weight": 0.15},
            "Humanities": {"academic_weight": 0.5, "activity_weight": 0.3, "misc_weight": 0.2},
            "Social Sciences": {"academic_weight": 0.55, "activity_weight": 0.25, "misc_weight": 0.2},
            "Arts": {"academic_weight": 0.45, "activity_weight": 0.35, "misc_weight": 0.2},
            "Business": {"academic_weight": 0.6, "activity_weight": 0.25, "misc_weight": 0.15},
            "Pre-Med/Health": {"academic_weight": 0.6, "activity_weight": 0.25, "misc_weight": 0.15},
            "Undecided": {"academic_weight": 0.55, "activity_weight": 0.25, "misc_weight": 0.2}
        }
    },
    "University of Virginia": {
        "avg_sat": 1390,
        "avg_gpa": 4.0,
        "selectivity": 0.24,
        "major_weights": {
            "STEM": {"academic_weight": 0.55, "activity_weight": 0.3, "misc_weight": 0.15},
            "Humanities": {"academic_weight": 0.45, "activity_weight": 0.35, "misc_weight": 0.2},
            "Social Sciences": {"academic_weight": 0.5, "activity_weight": 0.3, "misc_weight": 0.2},
            "Arts": {"academic_weight": 0.4, "activity_weight": 0.4, "misc_weight": 0.2},
            "Business": {"academic_weight": 0.55, "activity_weight": 0.3, "misc_weight": 0.15},
            "Pre-Med/Health": {"academic_weight": 0.55, "activity_weight": 0.3, "misc_weight": 0.15},
            "Undecided": {"academic_weight": 0.5, "activity_weight": 0.3, "misc_weight": 0.2}
        }
    }
}