"""
Admission probability simulator.
"""


import math
from college_data import COLLEGES, get_major_category
from typing import List, Dict, Any
from dataclasses import dataclass


# Scoring constants
EXTRACURRICULAR_CATEGORIES = {
    "Sports": 3,
    "Music": 2,
    "Arts": 2,
    "Volunteering": 2,
    "Clubs": 1,
    "Leadership": 3,
    "Academic": 2,
    "Research": 3,
    "Entrepreneurship": 3,
    "Other": 1
}


AWARD_LEVELS = {
    "local": 1,
    "regional": 2,
    "national": 3,
    "international": 4
}


@dataclass
class Student:
    """Student data class for admission simulation."""
    sat_score: int
    gpa: float
    class_rank_percentile: float  # 0-100, higher is better
    course_rigor: int  # 1-10
    intended_major: str
    extracurriculars: List[Dict[str, Any]]
    awards: List[Dict[str, Any]]
    legacy: bool = False
    faculty_child: bool = False
    recruited_athlete: bool = False
    
    def __post_init__(self):
        """Validate student data after initialization."""
        if not 400 <= self.sat_score <= 1600:
            raise ValueError(f"SAT score must be between 400 and 1600, got {self.sat_score}")
        if not 0.0 <= self.gpa <= 4.0:
            raise ValueError(f"GPA must be between 0.0 and 4.0, got {self.gpa}")
        if not 0 <= self.class_rank_percentile <= 100:
            raise ValueError(f"Class rank percentile must be between 0 and 100, got {self.class_rank_percentile}")
        if not 1 <= self.course_rigor <= 10:
            raise ValueError(f"Course rigor must be between 1 and 10, got {self.course_rigor}")
        if not self.intended_major:
            raise ValueError("Intended major cannot be empty")
        if not isinstance(self.extracurriculars, list):
            raise ValueError("Extracurriculars must be a list")
        if not isinstance(self.awards, list):
            raise ValueError("Awards must be a list")


class AdmissionSimulator:
    def __init__(self):
        # Default weights (used as fallback)
        self.default_weights = {
            "academic_weight": 0.5,
            "activity_weight": 0.3,
            "misc_weight": 0.2
        }
        
        # Minimum thresholds for different college tiers
        self.selectivity_thresholds = {
            "extremely selective": {"min_sat": 1450, "min_gpa": 3.8, "min_rank": 90},
            "very selective": {"min_sat": 1350, "min_gpa": 3.6, "min_rank": 80},
            "selective": {"min_sat": 1200, "min_gpa": 3.4, "min_rank": 70},
            "moderate": {"min_sat": 1050, "min_gpa": 3.0, "min_rank": 50},
            "less selective": {"min_sat": 900, "min_gpa": 2.5, "min_rank": 30}
        }

    def calculate_extracurricular_score(self, extracurriculars: List[Dict[str, Any]]) -> float:
        """
        Calculate score from extracurricular activities.
        
        :param extracurriculars: List of extracurricular activity dictionaries
        :return: Score between 0 and 50
        """
        if not extracurriculars:
            return 0.0
            
        total_score = 0.0
        for extra in extracurriculars:
            # Validate required fields
            if not all(k in extra for k in ['category', 'years', 'hours_per_week']):
                continue
                
            category_score = EXTRACURRICULAR_CATEGORIES.get(extra['category'], 1)
            years_factor = min(max(extra['years'], 0), 4) / 4  # Cap at 4 years
            hours_factor = min(max(extra['hours_per_week'], 0), 20) / 20  # Cap at 20 hours
            total_score += category_score * (years_factor + hours_factor)
            
        return min(total_score, 50)  # Cap total score

    def calculate_award_score(self, awards: List[Dict[str, Any]]) -> float:
        """
        Calculate score from awards.
        
        :param awards: List of award dictionaries
        :return: Score between 0 and 40
        """
        if not awards:
            return 0.0
            
        total_score = 0.0
        for award in awards:
            if 'level' not in award:
                continue
            total_score += AWARD_LEVELS.get(award['level'], 0)
            
        return min(total_score, 40)  # Cap at 40 (10 awards * 4 max)

    def calculate_academic_score(self, student: Student, college: Dict[str, Any]) -> float:
        """
        Calculate academic score relative to college.
        
        :param student: Student object
        :param college: College dictionary
        :return: Score between 0 and 1
        """
        # Normalize SAT score (400-1600 to 0-1)
        sat_normalized = (student.sat_score - 400) / 1200
        
        # Calculate SAT competitiveness relative to college average
        sat_gap = (student.sat_score - college['avg_sat']) / 1600
        sat_competitiveness = 0.5 + sat_gap  # Center around 0.5
        sat_competitiveness = max(0, min(1, sat_competitiveness))
        
        # Normalize GPA (0-4 to 0-1)
        gpa_normalized = student.gpa / 4.0
        
        # Calculate GPA competitiveness
        gpa_gap = (student.gpa - college['avg_gpa']) / 4.0
        gpa_competitiveness = 0.5 + gpa_gap
        gpa_competitiveness = max(0, min(1, gpa_competitiveness))
        
        # Class rank score (higher percentile = better)
        class_rank_score = student.class_rank_percentile / 100
        
        # Course rigor score (normalized to 0-1)
        course_rigor_score = min(max(student.course_rigor, 1), 10) / 10
        
        # Weighted academic components - all between 0 and 1
        academic_score = (
            0.3 * sat_competitiveness +
            0.3 * gpa_competitiveness +
            0.2 * class_rank_score +
            0.2 * course_rigor_score
        )
        
        return max(0, min(1, academic_score))

    def calculate_misc_bonus(self, student: Student) -> float:
        """
        Calculate bonus from legacy, athlete, etc.
        
        :param student: Student object
        :return: Bonus between 0 and 2
        """
        bonus = 0.0
        if student.legacy:
            bonus += 0.5
        if student.faculty_child:
            bonus += 0.3
        if student.recruited_athlete:
            bonus += 1.0
        return min(bonus, 2.0)  # Cap at 2.0

    def get_selectivity_bonus(self, student: Student, college: Dict[str, Any]) -> float:
        """
        Calculate bonus/penalty based on meeting selectivity thresholds.
        
        :param student: Student object
        :param college: College dictionary
        :return: Bonus factor between 0.8 and 1.2
        """
        selectivity = college.get('selectivity', 0.1)
        
        # Find closest selectivity tier
        closest_tier = None
        min_diff = float('inf')
        for tier, thresholds in self.selectivity_thresholds.items():
            diff = abs(selectivity - self.get_tier_selectivity(tier))
            if diff < min_diff:
                min_diff = diff
                closest_tier = tier
        
        if closest_tier:
            thresholds = self.selectivity_thresholds[closest_tier]
            meets_sat = student.sat_score >= thresholds['min_sat']
            meets_gpa = student.gpa >= thresholds['min_gpa']
            meets_rank = student.class_rank_percentile >= thresholds['min_rank']
            
            # Bonus for meeting all thresholds
            if meets_sat and meets_gpa and meets_rank:
                return 1.1
            # Penalty for missing all thresholds
            elif not (meets_sat or meets_gpa or meets_rank):
                return 0.85
        
        return 1.0

    def get_tier_selectivity(self, tier: str) -> float:
        """Get approximate selectivity rate for a tier."""
        tier_map = {
            "extremely selective": 0.05,
            "very selective": 0.15,
            "selective": 0.30,
            "moderate": 0.50,
            "less selective": 0.75
        }
        return tier_map.get(tier, 0.30)

    def calculate_holistic_score(self, student: Student, college: Dict[str, Any]) -> float:
        """
        Calculate holistic admission score considering all factors.
        
        :param student: Student object
        :param college: College dictionary
        :return: Score between 0 and 1
        """
        # Get major category and corresponding weights
        major_category = get_major_category(student.intended_major)
        weights = college.get('major_weights', {}).get(major_category, self.default_weights)
        
        # Calculate component scores
        academic_score = self.calculate_academic_score(student, college)
        
        # Calculate activity score (extracurriculars + awards)
        extracurricular_score = self.calculate_extracurricular_score(student.extracurriculars) / 50
        award_score = self.calculate_award_score(student.awards) / 40
        activity_score = (extracurricular_score + award_score) / 2
        
        misc_bonus = self.calculate_misc_bonus(student)
        
        # Composite score using major-specific weights
        composite_score = (
            weights['academic_weight'] * academic_score +
            weights['activity_weight'] * activity_score +
            weights['misc_weight'] * misc_bonus
        )
        
        # Apply selectivity bonus/penalty
        selectivity_bonus = self.get_selectivity_bonus(student, college)
        composite_score *= selectivity_bonus
        
        return max(0, min(1, composite_score))

    def calculate_probability(self, student: Student, college_name: str) -> float:
        """
        Calculate the probability of admission for a student to a college.
        
        :param student: Student object
        :param college_name: Name of the college
        :return: Probability as a float between 0 and 1
        """
        # Validate inputs
        if not isinstance(student, Student):
            raise TypeError(f"Expected Student object, got {type(student)}")
        
        if college_name not in COLLEGES:
            raise ValueError(f"College '{college_name}' not found.")
        
        college = COLLEGES[college_name]
        
        # Calculate holistic score
        holistic_score = self.calculate_holistic_score(student, college)
        
        # Adjust for college selectivity
        selectivity = college.get('selectivity', 0.3)
        
        # Use modified sigmoid function with base probability
        # Center the sigmoid around the college's base acceptance rate
        base_acceptance = selectivity
        
        # Scale factor determines how steep the probability curve is
        scale_factor = 8.0  # Higher = steeper curve
        
        # Calculate probability using logistic function
        # Shift the curve so that holistic_score = 0.5 maps to base_acceptance
        shift = math.log(base_acceptance / (1 - base_acceptance)) if 0 < base_acceptance < 1 else 0
        
        log_odds = scale_factor * (holistic_score - 0.5) + shift
        probability = 1 / (1 + math.exp(-log_odds))
        
        # Ensure probability stays within reasonable bounds
        probability = max(0.01, min(0.99, probability))
        
        return probability

    def compare_colleges(self, student: Student, college_names: List[str]) -> Dict[str, float]:
        """
        Compare admission probabilities across multiple colleges.
        
        :param student: Student object
        :param college_names: List of college names to compare
        :return: Dictionary of college names to probabilities, sorted by probability
        """
        results = {}
        errors = []
        
        for college_name in college_names:
            try:
                prob = self.calculate_probability(student, college_name)
                results[college_name] = prob
            except (ValueError, KeyError) as e:
                errors.append(f"{college_name}: {str(e)}")
        
        if errors:
            print("Warnings for some colleges:")
            for error in errors:
                print(f"  - {error}")
        
        # Sort by probability (highest first)
        return dict(sorted(results.items(), key=lambda x: x[1], reverse=True))

    def get_admission_category(self, probability: float) -> str:
        """
        Get admission category based on probability.
        
        :param probability: Admission probability between 0 and 1
        :return: Category string
        """
        if probability >= 0.75:
            return "Safety School (High Chance)"
        elif probability >= 0.50:
            return "Target School (Good Chance)"
        elif probability >= 0.25:
            return "Reach School (Low Chance)"
        else:
            return "Dream School (Very Low Chance)"

    def generate_report(self, student: Student, college_names: List[str]) -> str:
        """
        Generate a detailed admission report.
        
        :param student: Student object
        :param college_names: List of college names to evaluate
        :return: Formatted report string
        """
        report = []
        report.append("=" * 80)
        report.append("ADMISSION PROBABILITY REPORT")
        report.append("=" * 80)
        report.append("")
        
        # Student profile summary
        report.append("STUDENT PROFILE:")
        report.append(f"  SAT Score: {student.sat_score}/1600")
        report.append(f"  GPA: {student.gpa:.2f}/4.0")
        report.append(f"  Class Rank: Top {100 - student.class_rank_percentile:.0f}%")
        report.append(f"  Course Rigor: {student.course_rigor}/10")
        report.append(f"  Intended Major: {student.intended_major}")
        report.append(f"  Extracurriculars: {len(student.extracurriculars)} activities")
        report.append(f"  Awards: {len(student.awards)} awards")
        report.append(f"  Legacy: {'Yes' if student.legacy else 'No'}")
        report.append(f"  Recruited Athlete: {'Yes' if student.recruited_athlete else 'No'}")
        report.append("")
        
        # Calculate probabilities
        results = self.compare_colleges(student, college_names)
        
        # College comparison
        report.append("ADMISSION PROBABILITIES:")
        report.append("-" * 80)
        report.append(f"{'College':<30} {'Probability':<15} {'Category':<30}")
        report.append("-" * 80)
        
        for college_name, prob in results.items():
            category = self.get_admission_category(prob)
            report.append(f"{college_name:<30} {prob*100:>6.1f}%{'':<6} {category:<30}")
        
        report.append("=" * 80)
        
        # Add recommendations
        report.append("\nRECOMMENDATIONS:")
        safety_schools = [name for name, prob in results.items() if prob >= 0.75]
        target_schools = [name for name, prob in results.items() if 0.5 <= prob < 0.75]
        reach_schools = [name for name, prob in results.items() if 0.25 <= prob < 0.5]
        
        if safety_schools:
            report.append(f"  ✓ Safety Schools: {', '.join(safety_schools)}")
        if target_schools:
            report.append(f"  ✓ Target Schools: {', '.join(target_schools)}")
        if reach_schools:
            report.append(f"  ! Reach Schools: {', '.join(reach_schools)} - Consider adding more safeties/targets")
        
        report.append("\nNote: These probabilities are estimates based on historical data")
        report.append("and should be used as a guideline, not a guarantee of admission.")
        
        return "\n".join(report)


# Example usage
if __name__ == "__main__":
    # Create a sample student
    sample_student = Student(
        sat_score=1480,
        gpa=3.95,
        class_rank_percentile=96,
        course_rigor=9,
        intended_major="Computer Science",
        extracurriculars=[
            {"category": "Leadership", "years": 3, "hours_per_week": 10},
            {"category": "Academic", "years": 4, "hours_per_week": 8},
            {"category": "Sports", "years": 2, "hours_per_week": 15}
        ],
        awards=[
            {"level": "national"},
            {"level": "regional"},
            {"level": "local"}
        ],
        legacy=False,
        faculty_child=False,
        recruited_athlete=False
    )
    
    # Initialize simulator
    simulator = AdmissionSimulator()
    
    # Test with sample colleges (assuming they exist in college_data)
    sample_colleges = ["MIT", "Stanford", "Harvard", "UC Berkeley"]
    
    # Generate report
    report = simulator.generate_report(sample_student, sample_colleges)
    print(report)
    
    # Individual probability calculation
    print("\n" + "=" * 80)
    print("INDIVIDUAL COLLEGE PROBABILITY:")
    try:
        prob = simulator.calculate_probability(sample_student, "MIT")
        print(f"Probability of admission to MIT: {prob:.1%}")
    except ValueError as e:
        print(f"Error: {e}")