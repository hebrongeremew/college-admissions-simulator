"""
Student profile module.
"""

class Student:
    def __init__(self, name, age, gender, state, country,
                 underrepresented, rural_state, figli,
                 gpa, sat_score, class_rank_percentile, school_rank, course_rigor,
                 intended_major, extracurriculars, awards,
                 legacy, faculty_child, recruited_athlete):
        """
        Initialize a comprehensive student profile.

        Demographics:
        :param name: Student's name
        :param age: Age
        :param gender: Gender
        :param state: State (if applicable)
        :param country: Country
        :param underrepresented: Underrepresented group status (Y/N)
        :param rural_state: Rural state student status (Y/N)
        :param figli: First-generation low-income status (Y/N)

        Academic:
        :param gpa: GPA (0.0-4.0)
        :param sat_score: SAT score (400-1600)
        :param class_rank_percentile: Class rank percentile (0-100)
        :param school_rank: School ranking within sta
        te
        :param course_rigor: Number of AP/IB/Honor classes
        :param intended_major: Intended field of study/major

        Activities:
        :param extracurriculars: List of dicts with 'category', 'years', 'hours_per_week'
        :param awards: List of dicts with 'level' (local/regional/national/international)

        Misc:
        :param legacy: Legacy status (Y/N)
        :param faculty_child: Child of faculty (Y/N)
        :param recruited_athlete: Recruited athlete (Y/N)
        """
        # Demographics
        self.name = name
        self.age = age
        self.gender = gender
        self.state = state
        self.country = country
        self.underrepresented = underrepresented.upper() == 'Y'
        self.rural_state = rural_state.upper() == 'Y'
        self.figli = figli.upper() == 'Y'

        # Academic
        self.gpa = gpa
        self.sat_score = sat_score
        self.class_rank_percentile = class_rank_percentile
        self.school_rank = school_rank
        self.course_rigor = course_rigor
        self.intended_major = intended_major

        # Activities
        self.extracurriculars = extracurriculars  # list of dicts
        self.awards = awards  # list of dicts

        # Misc
        self.legacy = legacy.upper() == 'Y'
        self.faculty_child = faculty_child.upper() == 'Y'
        self.recruited_athlete = recruited_athlete.upper() == 'Y'

    def __str__(self):
        return f"Name: {self.name}, SAT: {self.sat_score}, GPA: {self.gpa}, Class Rank: {self.class_rank_percentile}%, Legacy: {self.legacy}, Athlete: {self.recruited_athlete}"