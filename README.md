# College Admission Simulator

"Chance me" - Calculate your probability of admission to top colleges!

## Description
This simulator calculates the probability of getting into a specific college based on a comprehensive student profile. Factors considered include demographics, academic performance, extracurricular activities, awards, and special circumstances.

## Features
- Interactive CLI for detailed student profile input
- Comprehensive scoring system considering:
  - Academic metrics (SAT, GPA, class rank, course rigor)
  - Extracurricular activities (unlimited entries with categories and time commitment)
  - Awards and honors (unlimited entries with local to international levels)
  - Special factors (legacy, recruited athlete, faculty child, underrepresented status)
  - **Major-specific weighting**: Different colleges weight factors differently based on intended field of study
- College-specific legacy and family connection questions
- Probability calculation with qualitative assessment (e.g., "Excellent chance", "Low chance")
- Selection from a list of prestigious colleges

## Usage
1. Run the simulator: `python main.py`
2. Enter comprehensive profile information:
   - Demographics (name, age, gender, location, underrepresented, rural state, FIGLI status)
   - Academic details (GPA, SAT, class rank, school ranking, AP/IB courses)
   - Extracurricular activities (unlimited entries with categories and time commitment)
   - Awards and honors (unlimited entries with recognition levels)
3. Select a college from the list
4. Answer college-specific questions (legacy status, faculty connections, recruited athlete)
5. View your calculated admission probability with qualitative assessment

## Scoring System
- **Extracurricular Categories**: Sports (3 pts), Leadership (3 pts), Research (3 pts), Music/Arts (2 pts), Volunteering (2 pts), Academic (2 pts), Clubs (1 pt)
- **Award Levels**: Local (1 pt), Regional (2 pts), National (3 pts), International (4 pts)
- **Special Bonuses**: Legacy (+0.5), Faculty Child (+0.3), Recruited Athlete (+1.0)

## Major-Specific Weighting
Different colleges prioritize different factors based on your intended major:

- **STEM majors** (Computer Science, Engineering, Math, etc.): Higher weight on academic performance
- **Humanities majors** (English, History, Philosophy, etc.): Balanced emphasis on academics and activities
- **Arts majors** (Fine Arts, Music, Theater, etc.): Higher weight on extracurricular activities
- **Business majors**: Strong academic focus with some activity consideration
- **Pre-Med/Health majors**: Heavy academic weighting

For example, MIT gives 70% weight to academics for STEM majors, while Yale gives 40% weight to activities for Arts majors.
- `main.py`: Main script with CLI interface
- `student.py`: Student profile class
- `simulator.py`: Admission probability calculation logic
- `college_data.py`: College data and statistics

## Requirements
- Python 3.6 or higher


