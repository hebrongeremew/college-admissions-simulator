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
        "avg_sat_math": 780,
        "avg_sat_rw": 760,
        "avg_act": 35,
        "avg_gpa": 3.9,
        "selectivity": 0.04,
        "major_weights": {
            "STEM": {"academic_weight": 0.6, "activity_weight": 0.25, "misc_weight": 0.15},
            "Humanities": {"academic_weight": 0.45, "activity_weight": 0.35, "misc_weight": 0.2},
            "Social Sciences": {"academic_weight": 0.5, "activity_weight": 0.3, "misc_weight": 0.2},
            "Arts": {"academic_weight": 0.4, "activity_weight": 0.4, "misc_weight": 0.2},
            "Business": {"academic_weight": 0.55, "activity_weight": 0.3, "misc_weight": 0.15},
            "Pre-Med/Health": {"academic_weight": 0.6, "activity_weight": 0.25, "misc_weight": 0.15},
            "Undecided": {"academic_weight": 0.5, "activity_weight": 0.3, "misc_weight": 0.2}
        },
        "sat_math_weight": 0.45,
        "sat_rw_weight": 0.55,
        "preferences": {
            "leadership": 1.25,
            "research": 1.10,
            "volunteering": 1.15,
            "sports": 1.10,
            "arts": 1.10
        }
    },
    "Stanford University": {
        "avg_sat_math": 790,
        "avg_sat_rw": 760,
        "avg_act": 34.5,
        "avg_gpa": 3.9,
        "selectivity": 0.04,
        "major_weights": {
            "STEM": {"academic_weight": 0.65, "activity_weight": 0.2, "misc_weight": 0.15},
            "Humanities": {"academic_weight": 0.45, "activity_weight": 0.35, "misc_weight": 0.2},
            "Social Sciences": {"academic_weight": 0.5, "activity_weight": 0.3, "misc_weight": 0.2},
            "Arts": {"academic_weight": 0.4, "activity_weight": 0.4, "misc_weight": 0.2},
            "Business": {"academic_weight": 0.55, "activity_weight": 0.3, "misc_weight": 0.15},
            "Pre-Med/Health": {"academic_weight": 0.6, "activity_weight": 0.25, "misc_weight": 0.15},
            "Undecided": {"academic_weight": 0.5, "activity_weight": 0.3, "misc_weight": 0.2}
        },
        "sat_math_weight": 0.55,
        "sat_rw_weight": 0.45,
        "preferences": {
            "research": 1.20,
            "leadership": 1.15,
            "entrepreneurship": 1.25,
            "sports": 1.10,
            "academic": 1.10
        }
    },
    "MIT": {
        "avg_sat_math": 790,
        "avg_sat_rw": 760,
        "avg_act": 35,
        "avg_gpa": 3.9,
        "selectivity": 0.05,
        "major_weights": {
            "STEM": {"academic_weight": 0.7, "activity_weight": 0.15, "misc_weight": 0.15},
            "Humanities": {"academic_weight": 0.5, "activity_weight": 0.3, "misc_weight": 0.2},
            "Social Sciences": {"academic_weight": 0.55, "activity_weight": 0.25, "misc_weight": 0.2},
            "Arts": {"academic_weight": 0.45, "activity_weight": 0.35, "misc_weight": 0.2},
            "Business": {"academic_weight": 0.6, "activity_weight": 0.25, "misc_weight": 0.15},
            "Pre-Med/Health": {"academic_weight": 0.65, "activity_weight": 0.2, "misc_weight": 0.15},
            "Undecided": {"academic_weight": 0.55, "activity_weight": 0.25, "misc_weight": 0.2}
        },
        "sat_math_weight": 0.65,
        "sat_rw_weight": 0.35,
        "preferences": {
            "research": 1.30,
            "academic": 1.25,
            "leadership": 1.10,
            "clubs": 1.05
        }
    },
    "Yale University": {
        "avg_sat_math": 780,
        "avg_sat_rw": 760,
        "avg_act": 34,
        "avg_gpa": 3.9,
        "selectivity": 0.04,
        "major_weights": {
            "STEM": {"academic_weight": 0.55, "activity_weight": 0.3, "misc_weight": 0.15},
            "Humanities": {"academic_weight": 0.4, "activity_weight": 0.4, "misc_weight": 0.2},
            "Social Sciences": {"academic_weight": 0.45, "activity_weight": 0.35, "misc_weight": 0.2},
            "Arts": {"academic_weight": 0.35, "activity_weight": 0.45, "misc_weight": 0.2},
            "Business": {"academic_weight": 0.5, "activity_weight": 0.3, "misc_weight": 0.2},
            "Pre-Med/Health": {"academic_weight": 0.55, "activity_weight": 0.3, "misc_weight": 0.15},
            "Undecided": {"academic_weight": 0.45, "activity_weight": 0.35, "misc_weight": 0.2}
        },
        "sat_math_weight": 0.48,
        "sat_rw_weight": 0.52,
        "preferences": {
            "leadership": 1.15,
            "research": 1.20,
            "arts": 1.20,
            "volunteering": 1.15,
            "music": 1.15
        }
    },
    "Princeton University": {
        "avg_sat_math": 780,
        "avg_sat_rw": 760,
        "avg_act": 34.5,
        "avg_gpa": 3.9,
        "selectivity": 0.05,
        "major_weights": {
            "STEM": {"academic_weight": 0.6, "activity_weight": 0.25, "misc_weight": 0.15},
            "Humanities": {"academic_weight": 0.45, "activity_weight": 0.35, "misc_weight": 0.2},
            "Social Sciences": {"academic_weight": 0.5, "activity_weight": 0.3, "misc_weight": 0.2},
            "Arts": {"academic_weight": 0.4, "activity_weight": 0.4, "misc_weight": 0.2},
            "Business": {"academic_weight": 0.55, "activity_weight": 0.3, "misc_weight": 0.15},
            "Pre-Med/Health": {"academic_weight": 0.6, "activity_weight": 0.25, "misc_weight": 0.15},
            "Undecided": {"academic_weight": 0.5, "activity_weight": 0.3, "misc_weight": 0.2}
        },
        "sat_math_weight": 0.52,
        "sat_rw_weight": 0.48,
        "preferences": {
            "research": 1.25,
            "academic": 1.20,
            "leadership": 1.10,
            "volunteering": 1.05,
            "sports": 1.05
        }
    },
    "University of California, Berkeley": {
        "avg_sat_math": 0,
        "avg_sat_rw": 0,
        "avg_act": 0,
        "avg_gpa": 3.9,
        "selectivity": 0.11,
        "major_weights": {
            "STEM": {"academic_weight": 0.65, "activity_weight": 0.2, "misc_weight": 0.15},
            "Humanities": {"academic_weight": 0.5, "activity_weight": 0.3, "misc_weight": 0.2},
            "Social Sciences": {"academic_weight": 0.55, "activity_weight": 0.25, "misc_weight": 0.2},
            "Arts": {"academic_weight": 0.45, "activity_weight": 0.35, "misc_weight": 0.2},
            "Business": {"academic_weight": 0.6, "activity_weight": 0.25, "misc_weight": 0.15},
            "Pre-Med/Health": {"academic_weight": 0.65, "activity_weight": 0.2, "misc_weight": 0.15},
            "Undecided": {"academic_weight": 0.55, "activity_weight": 0.25, "misc_weight": 0.2}
        },
        "sat_math_weight": 0,
        "sat_rw_weight": 0,
        "preferences": {
            "research": 1.20,
            "academic": 1.15,
            "leadership": 1.10,
            "volunteering": 1.10
        }
    },
    "University of Michigan": {
        "avg_sat_math": 740,
        "avg_sat_rw": 720,
        "avg_act": 32.5,
        "avg_gpa": 3.9,
        "selectivity": 0.16,
        "major_weights": {
            "STEM": {"academic_weight": 0.6, "activity_weight": 0.25, "misc_weight": 0.15},
            "Humanities": {"academic_weight": 0.5, "activity_weight": 0.3, "misc_weight": 0.2},
            "Social Sciences": {"academic_weight": 0.55, "activity_weight": 0.25, "misc_weight": 0.2},
            "Arts": {"academic_weight": 0.45, "activity_weight": 0.35, "misc_weight": 0.2},
            "Business": {"academic_weight": 0.6, "activity_weight": 0.25, "misc_weight": 0.15},
            "Pre-Med/Health": {"academic_weight": 0.6, "activity_weight": 0.25, "misc_weight": 0.15},
            "Undecided": {"academic_weight": 0.55, "activity_weight": 0.25, "misc_weight": 0.2}
        },
        "sat_math_weight": 0.50,
        "sat_rw_weight": 0.50,
        "preferences": {
            "leadership": 1.15,
            "sports": 1.10,
            "research": 1.10,
            "volunteering": 1.10
        }
    },
    "Columbia University": {
        "avg_sat_math": 779,
        "avg_sat_rw": 757,
        "avg_act": 34.5,
        "avg_gpa": 3.9,
        "selectivity": 0.04,
        "major_weights": {
            "STEM": {"academic_weight": 0.6, "activity_weight": 0.25, "misc_weight": 0.15},
            "Humanities": {"academic_weight": 0.45, "activity_weight": 0.35, "misc_weight": 0.2},
            "Social Sciences": {"academic_weight": 0.5, "activity_weight": 0.3, "misc_weight": 0.2},
            "Arts": {"academic_weight": 0.4, "activity_weight": 0.4, "misc_weight": 0.2},
            "Business": {"academic_weight": 0.55, "activity_weight": 0.3, "misc_weight": 0.15},
            "Pre-Med/Health": {"academic_weight": 0.6, "activity_weight": 0.25, "misc_weight": 0.15},
            "Undecided": {"academic_weight": 0.5, "activity_weight": 0.3, "misc_weight": 0.2}
        },
        "sat_math_weight": 0.50,
        "sat_rw_weight": 0.50,
        "preferences": {
            "research": 1.15,
            "leadership": 1.20,
            "internships": 1.25,
            "volunteering": 1.10,
            "arts": 1.10
        }
    },
    "University of Pennsylvania": {
        "avg_sat_math": 790,
        "avg_sat_rw": 760,
        "avg_act": 35,
        "avg_gpa": 3.9,
        "selectivity": 0.05,
        "major_weights": {
            "STEM": {"academic_weight": 0.6, "activity_weight": 0.25, "misc_weight": 0.15},
            "Humanities": {"academic_weight": 0.45, "activity_weight": 0.35, "misc_weight": 0.2},
            "Social Sciences": {"academic_weight": 0.5, "activity_weight": 0.3, "misc_weight": 0.2},
            "Arts": {"academic_weight": 0.4, "activity_weight": 0.4, "misc_weight": 0.2},
            "Business": {"academic_weight": 0.6, "activity_weight": 0.3, "misc_weight": 0.1},
            "Pre-Med/Health": {"academic_weight": 0.6, "activity_weight": 0.25, "misc_weight": 0.15},
            "Undecided": {"academic_weight": 0.5, "activity_weight": 0.3, "misc_weight": 0.2}
        },
        "sat_math_weight": 0.53,
        "sat_rw_weight": 0.47,
        "preferences": {
            "leadership": 1.30,
            "internships": 1.30,
            "entrepreneurship": 1.25,
            "business": 1.25,
            "research": 1.05
        }
    },
    "Brown University": {
        "avg_sat_math": 780,
        "avg_sat_rw": 760,
        "avg_act": 34.5,
        "avg_gpa": 3.9,
        "selectivity": 0.05,
        "major_weights": {
            "STEM": {"academic_weight": 0.55, "activity_weight": 0.3, "misc_weight": 0.15},
            "Humanities": {"academic_weight": 0.4, "activity_weight": 0.4, "misc_weight": 0.2},
            "Social Sciences": {"academic_weight": 0.45, "activity_weight": 0.35, "misc_weight": 0.2},
            "Arts": {"academic_weight": 0.35, "activity_weight": 0.45, "misc_weight": 0.2},
            "Business": {"academic_weight": 0.5, "activity_weight": 0.3, "misc_weight": 0.2},
            "Pre-Med/Health": {"academic_weight": 0.55, "activity_weight": 0.3, "misc_weight": 0.15},
            "Undecided": {"academic_weight": 0.45, "activity_weight": 0.35, "misc_weight": 0.2}
        },
        "sat_math_weight": 0.47,
        "sat_rw_weight": 0.53,
        "preferences": {
            "arts": 1.20,
            "volunteering": 1.20,
            "leadership": 1.10,
            "research": 1.10,
            "nontraditional": 1.25
        }
    },
    "Cornell University": {
        "avg_sat_math": 790,
        "avg_sat_rw": 750,
        "avg_act": 34,
        "avg_gpa": 3.85,
        "selectivity": 0.08,
        "major_weights": {
            "STEM": {"academic_weight": 0.65, "activity_weight": 0.2, "misc_weight": 0.15},
            "Humanities": {"academic_weight": 0.5, "activity_weight": 0.3, "misc_weight": 0.2},
            "Social Sciences": {"academic_weight": 0.55, "activity_weight": 0.25, "misc_weight": 0.2},
            "Arts": {"academic_weight": 0.45, "activity_weight": 0.35, "misc_weight": 0.2},
            "Business": {"academic_weight": 0.6, "activity_weight": 0.25, "misc_weight": 0.15},
            "Pre-Med/Health": {"academic_weight": 0.6, "activity_weight": 0.25, "misc_weight": 0.15},
            "Undecided": {"academic_weight": 0.55, "activity_weight": 0.25, "misc_weight": 0.2}
        },
        "sat_math_weight": 0.55,
        "sat_rw_weight": 0.45,
        "preferences": {
            "research": 1.20,
            "academic": 1.20,
            "engineering": 1.25,
            "leadership": 1.10,
            "volunteering": 1.05,
            "arts": 1.00
        }
    },
    "Dartmouth College": {
        "avg_sat_math": 760,
        "avg_sat_rw": 740,
        "avg_act": 34,
        "avg_gpa": 3.85,
        "selectivity": 0.05,
        "major_weights": {
            "STEM": {"academic_weight": 0.55, "activity_weight": 0.3, "misc_weight": 0.15},
            "Humanities": {"academic_weight": 0.4, "activity_weight": 0.4, "misc_weight": 0.2},
            "Social Sciences": {"academic_weight": 0.45, "activity_weight": 0.35, "misc_weight": 0.2},
            "Arts": {"academic_weight": 0.35, "activity_weight": 0.45, "misc_weight": 0.2},
            "Business": {"academic_weight": 0.5, "activity_weight": 0.3, "misc_weight": 0.2},
            "Pre-Med/Health": {"academic_weight": 0.55, "activity_weight": 0.3, "misc_weight": 0.15},
            "Undecided": {"academic_weight": 0.45, "activity_weight": 0.35, "misc_weight": 0.2}
        },
        "sat_math_weight": 0.50,
        "sat_rw_weight": 0.50,
        "preferences": {
            "leadership": 1.25,
            "volunteering": 1.20,
            "sports": 1.15,
            "outdoors": 1.30,
            "community": 1.25,
            "research": 1.10
        }
    },
    "University of Chicago": {
        "avg_sat_math": 790,
        "avg_sat_rw": 760,
        "avg_act": 34.5,
        "avg_gpa": 3.9,
        "selectivity": 0.04,
        "major_weights": {
            "STEM": {"academic_weight": 0.6, "activity_weight": 0.25, "misc_weight": 0.15},
            "Humanities": {"academic_weight": 0.45, "activity_weight": 0.35, "misc_weight": 0.2},
            "Social Sciences": {"academic_weight": 0.5, "activity_weight": 0.3, "misc_weight": 0.2},
            "Arts": {"academic_weight": 0.4, "activity_weight": 0.4, "misc_weight": 0.2},
            "Business": {"academic_weight": 0.55, "activity_weight": 0.3, "misc_weight": 0.15},
            "Pre-Med/Health": {"academic_weight": 0.6, "activity_weight": 0.25, "misc_weight": 0.15},
            "Undecided": {"academic_weight": 0.5, "activity_weight": 0.3, "misc_weight": 0.2}
        },
        "sat_math_weight": 0.50,
        "sat_rw_weight": 0.50,
        "preferences": {
            "academic": 1.30,
            "research": 1.20,
            "leadership": 1.10,
            "writing": 1.25
        }
    },
    "Duke University": {
        "avg_sat_math": 780,
        "avg_sat_rw": 740,
        "avg_act": 34.5,
        "avg_gpa": 3.85,
        "selectivity": 0.06,
        "major_weights": {
            "STEM": {"academic_weight": 0.6, "activity_weight": 0.25, "misc_weight": 0.15},
            "Humanities": {"academic_weight": 0.45, "activity_weight": 0.35, "misc_weight": 0.2},
            "Social Sciences": {"academic_weight": 0.5, "activity_weight": 0.3, "misc_weight": 0.2},
            "Arts": {"academic_weight": 0.4, "activity_weight": 0.4, "misc_weight": 0.2},
            "Business": {"academic_weight": 0.55, "activity_weight": 0.3, "misc_weight": 0.15},
            "Pre-Med/Health": {"academic_weight": 0.6, "activity_weight": 0.25, "misc_weight": 0.15},
            "Undecided": {"academic_weight": 0.5, "activity_weight": 0.3, "misc_weight": 0.2}
        },
        "sat_math_weight": 0.50,
        "sat_rw_weight": 0.50,
        "preferences": {
            "leadership": 1.25,
            "sports": 1.20,
            "research": 1.15,
            "community": 1.15
        }
    },
    "Northwestern University": {
        "avg_sat_math": 780,
        "avg_sat_rw": 750,
        "avg_act": 34.5,
        "avg_gpa": 3.85,
        "selectivity": 0.08,
        "major_weights": {
            "STEM": {"academic_weight": 0.6, "activity_weight": 0.25, "misc_weight": 0.15},
            "Humanities": {"academic_weight": 0.45, "activity_weight": 0.35, "misc_weight": 0.2},
            "Social Sciences": {"academic_weight": 0.5, "activity_weight": 0.3, "misc_weight": 0.2},
            "Arts": {"academic_weight": 0.4, "activity_weight": 0.4, "misc_weight": 0.2},
            "Business": {"academic_weight": 0.55, "activity_weight": 0.3, "misc_weight": 0.15},
            "Pre-Med/Health": {"academic_weight": 0.6, "activity_weight": 0.25, "misc_weight": 0.15},
            "Undecided": {"academic_weight": 0.5, "activity_weight": 0.3, "misc_weight": 0.2}
        },
        "sat_math_weight": 0.50,
        "sat_rw_weight": 0.50,
        "preferences": {
            "journalism": 1.25,
            "arts": 1.20,
            "leadership": 1.15,
            "research": 1.10
        }
    },

    "California Institute of Technology": {
        "avg_sat_math": 795,
        "avg_sat_rw": 750,
        "avg_act": 35,
        "avg_gpa": 3.9,
        "selectivity": 0.03,
        "major_weights": {
            "STEM": {"academic_weight": 0.75, "activity_weight": 0.15, "misc_weight": 0.10},
            "Humanities": {"academic_weight": 0.6, "activity_weight": 0.25, "misc_weight": 0.15},
            "Social Sciences": {"academic_weight": 0.65, "activity_weight": 0.2, "misc_weight": 0.15},
            "Arts": {"academic_weight": 0.5, "activity_weight": 0.35, "misc_weight": 0.15},
            "Business": {"academic_weight": 0.65, "activity_weight": 0.2, "misc_weight": 0.15},
            "Pre-Med/Health": {"academic_weight": 0.7, "activity_weight": 0.2, "misc_weight": 0.1},
            "Undecided": {"academic_weight": 0.65, "activity_weight": 0.2, "misc_weight": 0.15}
        },
        "sat_math_weight": 0.70,
        "sat_rw_weight": 0.30,
        "preferences": {
            "research": 1.35,
            "academic": 1.30,
            "math": 1.35
        }
    },

    "Johns Hopkins University": {
        "avg_sat_math": 790,
        "avg_sat_rw": 760,
        "avg_act": 35,
        "avg_gpa": 3.9,
        "selectivity": 0.06,
        "major_weights": {
            "STEM": {"academic_weight": 0.65, "activity_weight": 0.2, "misc_weight": 0.15},
            "Humanities": {"academic_weight": 0.45, "activity_weight": 0.35, "misc_weight": 0.2},
            "Social Sciences": {"academic_weight": 0.5, "activity_weight": 0.3, "misc_weight": 0.2},
            "Arts": {"academic_weight": 0.4, "activity_weight": 0.4, "misc_weight": 0.2},
            "Business": {"academic_weight": 0.55, "activity_weight": 0.3, "misc_weight": 0.15},
            "Pre-Med/Health": {"academic_weight": 0.7, "activity_weight": 0.2, "misc_weight": 0.1},
            "Undecided": {"academic_weight": 0.5, "activity_weight": 0.3, "misc_weight": 0.2}
        },
        "sat_math_weight": 0.55,
        "sat_rw_weight": 0.45,
        "preferences": {
            "research": 1.30,
            "health": 1.30,
            "volunteering": 1.20
        }
    },

    "Rice University": {
        "avg_sat_math": 785,
        "avg_sat_rw": 755,
        "avg_act": 34.5,
        "avg_gpa": 3.85,
        "selectivity": 0.08,
        "major_weights": {
            "STEM": {"academic_weight": 0.6, "activity_weight": 0.25, "misc_weight": 0.15},
            "Humanities": {"academic_weight": 0.45, "activity_weight": 0.35, "misc_weight": 0.2},
            "Social Sciences": {"academic_weight": 0.5, "activity_weight": 0.3, "misc_weight": 0.2},
            "Arts": {"academic_weight": 0.4, "activity_weight": 0.4, "misc_weight": 0.2},
            "Business": {"academic_weight": 0.55, "activity_weight": 0.3, "misc_weight": 0.15},
            "Pre-Med/Health": {"academic_weight": 0.6, "activity_weight": 0.25, "misc_weight": 0.15},
            "Undecided": {"academic_weight": 0.5, "activity_weight": 0.3, "misc_weight": 0.2}
        },
        "sat_math_weight": 0.52,
        "sat_rw_weight": 0.48,
        "preferences": {
            "research": 1.15,
            "community": 1.25,
            "leadership": 1.15
        }
    },

    "Vanderbilt University": {
        "avg_sat_math": 790,
        "avg_sat_rw": 750,
        "avg_act": 34.5,
        "avg_gpa": 3.8,
        "selectivity": 0.06,
        "major_weights": {
            "STEM": {"academic_weight": 0.6, "activity_weight": 0.25, "misc_weight": 0.15},
            "Humanities": {"academic_weight": 0.45, "activity_weight": 0.35, "misc_weight": 0.2},
            "Social Sciences": {"academic_weight": 0.5, "activity_weight": 0.3, "misc_weight": 0.2},
            "Arts": {"academic_weight": 0.4, "activity_weight": 0.4, "misc_weight": 0.2},
            "Business": {"academic_weight": 0.55, "activity_weight": 0.3, "misc_weight": 0.15},
            "Pre-Med/Health": {"academic_weight": 0.6, "activity_weight": 0.25, "misc_weight": 0.15},
            "Undecided": {"academic_weight": 0.5, "activity_weight": 0.3, "misc_weight": 0.2}
        },
        "sat_math_weight": 0.50,
        "sat_rw_weight": 0.50,
        "preferences": {
            "leadership": 1.25,
            "volunteering": 1.20,
            "community": 1.20
        }
    },
    "University of Chicago": {
        "avg_sat": 1520,
        "avg_gpa": 3.95,
        "selectivity": 0.05,
        "major_weights": {
            "STEM": {"academic_weight": 0.6, "activity_weight": 0.25, "misc_weight": 0.15},
            "Humanities": {"academic_weight": 0.45, "activity_weight": 0.35, "misc_weight": 0.2},
            "Social Sciences": {"academic_weight": 0.5, "activity_weight": 0.3, "misc_weight": 0.2},
            "Arts": {"academic_weight": 0.4, "activity_weight": 0.4, "misc_weight": 0.2},
            "Business": {"academic_weight": 0.55, "activity_weight": 0.3, "misc_weight": 0.15},
            "Pre-Med/Health": {"academic_weight": 0.6, "activity_weight": 0.25, "misc_weight": 0.15},
            "Undecided": {"academic_weight": 0.5, "activity_weight": 0.3, "misc_weight": 0.2}
        },
        "sat_math_weight": 0.50,
        "sat_rw_weight": 0.50,
        "preferences": {
            "academic": 1.30,
            "research": 1.20,
            "leadership": 1.10,
            "writing": 1.25
        }
    },
    "Duke University": {
        "avg_sat": 1510,
        "avg_gpa": 3.95,
        "selectivity": 0.06,
        "major_weights": {
            "STEM": {"academic_weight": 0.6, "activity_weight": 0.25, "misc_weight": 0.15},
            "Humanities": {"academic_weight": 0.45, "activity_weight": 0.35, "misc_weight": 0.2},
            "Social Sciences": {"academic_weight": 0.5, "activity_weight": 0.3, "misc_weight": 0.2},
            "Arts": {"academic_weight": 0.4, "activity_weight": 0.4, "misc_weight": 0.2},
            "Business": {"academic_weight": 0.55, "activity_weight": 0.3, "misc_weight": 0.15},
            "Pre-Med/Health": {"academic_weight": 0.6, "activity_weight": 0.25, "misc_weight": 0.15},
            "Undecided": {"academic_weight": 0.5, "activity_weight": 0.3, "misc_weight": 0.2}
        },
        "sat_math_weight": 0.50,
        "sat_rw_weight": 0.50,
        "preferences": {
            "leadership": 1.25,
            "sports": 1.20,
            "research": 1.15,
            "community": 1.15
        }
    },
    "Northwestern University": {
        "avg_sat": 1500,
        "avg_gpa": 3.93,
        "selectivity": 0.07,
        "major_weights": {
            "STEM": {"academic_weight": 0.6, "activity_weight": 0.25, "misc_weight": 0.15},
            "Humanities": {"academic_weight": 0.45, "activity_weight": 0.35, "misc_weight": 0.2},
            "Social Sciences": {"academic_weight": 0.5, "activity_weight": 0.3, "misc_weight": 0.2},
            "Arts": {"academic_weight": 0.4, "activity_weight": 0.4, "misc_weight": 0.2},
            "Business": {"academic_weight": 0.55, "activity_weight": 0.3, "misc_weight": 0.15},
            "Pre-Med/Health": {"academic_weight": 0.6, "activity_weight": 0.25, "misc_weight": 0.15},
            "Undecided": {"academic_weight": 0.5, "activity_weight": 0.3, "misc_weight": 0.2}
        },
        "sat_math_weight": 0.50,
        "sat_rw_weight": 0.50,
        "preferences": {
            "journalism": 1.25,
            "arts": 1.20,
            "leadership": 1.15,
            "research": 1.10
        }
    },
    "California Institute of Technology": {
        "avg_sat": 1540,
        "avg_gpa": 4.2,
        "selectivity": 0.04,
        "major_weights": {
            "STEM": {"academic_weight": 0.75, "activity_weight": 0.15, "misc_weight": 0.10},
            "Humanities": {"academic_weight": 0.6, "activity_weight": 0.25, "misc_weight": 0.15},
            "Social Sciences": {"academic_weight": 0.65, "activity_weight": 0.2, "misc_weight": 0.15},
            "Arts": {"academic_weight": 0.5, "activity_weight": 0.35, "misc_weight": 0.15},
            "Business": {"academic_weight": 0.65, "activity_weight": 0.2, "misc_weight": 0.15},
            "Pre-Med/Health": {"academic_weight": 0.7, "activity_weight": 0.2, "misc_weight": 0.1},
            "Undecided": {"academic_weight": 0.65, "activity_weight": 0.2, "misc_weight": 0.15}
        },
        "sat_math_weight": 0.70,
        "sat_rw_weight": 0.30,
        "preferences": {
            "research": 1.35,
            "academic": 1.30,
            "math": 1.35
        }
    },
    "Johns Hopkins University": {
        "avg_sat": 1520,
        "avg_gpa": 3.95,
        "selectivity": 0.05,
        "major_weights": {
            "STEM": {"academic_weight": 0.65, "activity_weight": 0.2, "misc_weight": 0.15},
            "Humanities": {"academic_weight": 0.45, "activity_weight": 0.35, "misc_weight": 0.2},
            "Social Sciences": {"academic_weight": 0.5, "activity_weight": 0.3, "misc_weight": 0.2},
            "Arts": {"academic_weight": 0.4, "activity_weight": 0.4, "misc_weight": 0.2},
            "Business": {"academic_weight": 0.55, "activity_weight": 0.3, "misc_weight": 0.15},
            "Pre-Med/Health": {"academic_weight": 0.7, "activity_weight": 0.2, "misc_weight": 0.1},
            "Undecided": {"academic_weight": 0.5, "activity_weight": 0.3, "misc_weight": 0.2}
        },
        "sat_math_weight": 0.55,
        "sat_rw_weight": 0.45,
        "preferences": {
            "research": 1.30,
            "health": 1.30,
            "volunteering": 1.20
        }
    },
    "Rice University": {
        "avg_sat": 1500,
        "avg_gpa": 3.93,
        "selectivity": 0.07,
        "major_weights": {
            "STEM": {"academic_weight": 0.6, "activity_weight": 0.25, "misc_weight": 0.15},
            "Humanities": {"academic_weight": 0.45, "activity_weight": 0.35, "misc_weight": 0.2},
            "Social Sciences": {"academic_weight": 0.5, "activity_weight": 0.3, "misc_weight": 0.2},
            "Arts": {"academic_weight": 0.4, "activity_weight": 0.4, "misc_weight": 0.2},
            "Business": {"academic_weight": 0.55, "activity_weight": 0.3, "misc_weight": 0.15},
            "Pre-Med/Health": {"academic_weight": 0.6, "activity_weight": 0.25, "misc_weight": 0.15},
            "Undecided": {"academic_weight": 0.5, "activity_weight": 0.3, "misc_weight": 0.2}
        },
        "sat_math_weight": 0.52,
        "sat_rw_weight": 0.48,
        "preferences": {
            "research": 1.15,
            "community": 1.25,
            "leadership": 1.15
        }
    },
    "Vanderbilt University": {
        "avg_sat": 1505,
        "avg_gpa": 3.93,
        "selectivity": 0.07,
        "major_weights": {
            "STEM": {"academic_weight": 0.6, "activity_weight": 0.25, "misc_weight": 0.15},
            "Humanities": {"academic_weight": 0.45, "activity_weight": 0.35, "misc_weight": 0.2},
            "Social Sciences": {"academic_weight": 0.5, "activity_weight": 0.3, "misc_weight": 0.2},
            "Arts": {"academic_weight": 0.4, "activity_weight": 0.4, "misc_weight": 0.2},
            "Business": {"academic_weight": 0.55, "activity_weight": 0.3, "misc_weight": 0.15},
            "Pre-Med/Health": {"academic_weight": 0.6, "activity_weight": 0.25, "misc_weight": 0.15},
            "Undecided": {"academic_weight": 0.5, "activity_weight": 0.3, "misc_weight": 0.2}
        },
        "sat_math_weight": 0.50,
        "sat_rw_weight": 0.50,
        "preferences": {
            "leadership": 1.25,
            "volunteering": 1.20,
            "community": 1.20
        }

    },
    "University of California, Los Angeles": {
        "avg_sat_math": 0,
        "avg_sat_rw": 0,
        "avg_act": 0,
        "avg_gpa": 3.9,
        "selectivity": 0.09,
        "major_weights": {
            "STEM": {"academic_weight": 0.6, "activity_weight": 0.25, "misc_weight": 0.15},
            "Humanities": {"academic_weight": 0.45, "activity_weight": 0.35, "misc_weight": 0.2},
            "Social Sciences": {"academic_weight": 0.5, "activity_weight": 0.3, "misc_weight": 0.2},
            "Arts": {"academic_weight": 0.4, "activity_weight": 0.4, "misc_weight": 0.2},
            "Business": {"academic_weight": 0.55, "activity_weight": 0.3, "misc_weight": 0.15},
            "Pre-Med/Health": {"academic_weight": 0.6, "activity_weight": 0.25, "misc_weight": 0.15},
            "Undecided": {"academic_weight": 0.5, "activity_weight": 0.3, "misc_weight": 0.2}
        },
        "sat_math_weight": 0,
        "sat_rw_weight": 0,
        "preferences": {
            "leadership": 1.25,
            "volunteering": 1.20,
            "community": 1.20
        }
    },
    "Carnegie Mellon University": {
        "avg_sat_math": 790,
        "avg_sat_rw": 750,
        "avg_act": 34.5,
        "avg_gpa": 3.9,
        "selectivity": 0.12,
        "major_weights": {
            "STEM": {"academic_weight": 0.6, "activity_weight": 0.25, "misc_weight": 0.15},
            "Humanities": {"academic_weight": 0.45, "activity_weight": 0.35, "misc_weight": 0.2},
            "Social Sciences": {"academic_weight": 0.5, "activity_weight": 0.3, "misc_weight": 0.2},
            "Arts": {"academic_weight": 0.4, "activity_weight": 0.4, "misc_weight": 0.2},
            "Business": {"academic_weight": 0.55, "activity_weight": 0.3, "misc_weight": 0.15},
            "Pre-Med/Health": {"academic_weight": 0.6, "activity_weight": 0.25, "misc_weight": 0.15},
            "Undecided": {"academic_weight": 0.5, "activity_weight": 0.3, "misc_weight": 0.2}
        },
        "sat_math_weight": 0.50,
        "sat_rw_weight": 0.50,
        "preferences": {
            "leadership": 1.25,
            "volunteering": 1.20,
            "community": 1.20
    
        }
    },
    "University of Notre Dame": {
        "avg_sat_math": 770,
        "avg_sat_rw": 750,
        "avg_act": 35,
        "avg_gpa": 3.85,
        "selectivity": 0.11,
        "major_weights": {
            "STEM": {"academic_weight": 0.6, "activity_weight": 0.25, "misc_weight": 0.15},
            "Humanities": {"academic_weight": 0.45, "activity_weight": 0.35, "misc_weight": 0.2},
            "Social Sciences": {"academic_weight": 0.5, "activity_weight": 0.3, "misc_weight": 0.2},
            "Arts": {"academic_weight": 0.4, "activity_weight": 0.4, "misc_weight": 0.2},
            "Business": {"academic_weight": 0.55, "activity_weight": 0.3, "misc_weight": 0.15},
            "Pre-Med/Health": {"academic_weight": 0.6, "activity_weight": 0.25, "misc_weight": 0.15},
            "Undecided": {"academic_weight": 0.5, "activity_weight": 0.3, "misc_weight": 0.2}
        },
        "sat_math_weight": 0.50,
        "sat_rw_weight": 0.50,
        "preferences": {
            "leadership": 1.25,
            "volunteering": 1.20,
            "community": 1.20
        }
    },
    "Washington University in St. Louis": {
        "avg_sat_math": 787,
        "avg_sat_rw": 747,
        "avg_act": 34,
        "avg_gpa": 3.9,
        "selectivity": 0.11,
        "major_weights": {
            "STEM": {"academic_weight": 0.6, "activity_weight": 0.25, "misc_weight": 0.15},
            "Humanities": {"academic_weight": 0.45, "activity_weight": 0.35, "misc_weight": 0.2},
            "Social Sciences": {"academic_weight": 0.5, "activity_weight": 0.3, "misc_weight": 0.2},
            "Arts": {"academic_weight": 0.4, "activity_weight": 0.4, "misc_weight": 0.2},
            "Business": {"academic_weight": 0.55, "activity_weight": 0.3, "misc_weight": 0.15},
            "Pre-Med/Health": {"academic_weight": 0.6, "activity_weight": 0.25, "misc_weight": 0.15},
            "Undecided": {"academic_weight": 0.5, "activity_weight": 0.3, "misc_weight": 0.2}
        },
        "sat_math_weight": 0.50,
        "sat_rw_weight": 0.50,
        "preferences": {
            "leadership": 1.25,
            "volunteering": 1.20,
            "community": 1.20
        }
    }

}
