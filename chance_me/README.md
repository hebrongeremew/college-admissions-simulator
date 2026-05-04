readme.md
# Chance Me

A college admissions simulator that helps students understand their acceptance chances at various universities.
## Project Structure

```
college-admissions-simulator/
├── chance_me/           # Main application module
├── data/                # University database and datasets
├── tests/               # Unit and integration tests
├── requirements.txt     # Python dependencies
├── app.py             # Application entry point
└── README.md           # Project documentation
```

## File Organization

- **chance_me/** - Core simulator logic and UI components
- **data/** - University profiles, admission statistics, and reference data
- **tests/** - Test suites for application functionality
- **requirements.txt** - Project dependencies and versions
- **app.py** - Application launcher
- **college_data.py** - College information
- **index.html** - Front-end building

## Features

- Interactive admissions calculator
- Multiple university database
- GPA and test score analysis
- Personalized recommendations

## Getting Started

1. Clone the repository and install dependencies (see Installation section)
2. Run `python main.py` to launch the application
3. Enter your academic profile (GPA, test scores)
4. Explore acceptance probabilities across universities
5. Review personalized recommendations based on your profile


### Prerequisites

- Python 3.8+
- pip package manager

### Installation

```bash
git clone https://github.com/hebrongeremew/college-admissions-simulator.git
cd college-admissions-simulator
pip install -r requirements.txt
```

### Usage

```bash
python main.py
```

### Troubleshooting

- If flask not found, run 'pip install flask'
- Ensure you are in the chance_me folder (run cd chance_me)
- Merge errors (Git conflicts)
  If you see lines with lots of `<`, `>`, or `=` (like merge conflict markers), delete them and keep the correct code.

    
   

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## External Contributers

- data for colleges
    - https://www.usnews.com/best-colleges/rankings/national-universities?myCollege=national-universities&_sort=myCollege&_sortDirection=asc 

    - https://www.zenithprepacademy.com/college-admissions/#princeton

- AI help
    _ claude inline editor (for HTML formatting and the formatting of repetive statements in app.py)
