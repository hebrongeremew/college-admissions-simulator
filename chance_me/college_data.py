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
        
        "academic_weight": 0.45,
        "activity_weight": 0.35,
        "misc_weight": 0.20,
            
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
        
        "academic_weight": 0.47,
        "activity_weight": 0.33,
        "misc_weight": 0.20,
        
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
        "academic_weight": 0.52,
        "activity_weight": 0.28,
        "misc_weight": 0.20,
        
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
    },
        
     "Columbia University": {
        "avg_sat": 1510,
        "avg_gpa": 3.95,
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
        "avg_sat": 1500,
        "avg_gpa": 3.93,
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
        "avg_sat": 1500,
        "avg_gpa": 3.95,
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
        "avg_sat": 1480,
        "avg_gpa": 3.9,
        "selectivity": 0.07,

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
        "avg_sat": 1500,
        "avg_gpa": 3.9,
        "selectivity": 0.06,

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
    }

}

    
    
    
    
    }
