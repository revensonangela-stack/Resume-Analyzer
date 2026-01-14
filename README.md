Resume Analyzer & Skill Gap Finder

📄 A Python-based Resume Analyzer that compares your resume against a job description and highlights matched and missing skills. Ideal for job seekers looking to optimize their resumes for specific roles.

Features
✅ Supports resume files in TXT, PDF, and DOCX formats
✅ Supports job description files in TXT, PDF, and DOCX formats
✅ Compares your resume skills against a predefined common skills list
✅ Identifies matched skills and missing skills
✅ Calculates skill match percentage
✅ Provides suggestions for skills to add or improve

Technology Stack
Python 3.8+

Libraries:
PyPDF2
 – for PDF text extraction
python-docx
 – for DOCX text extraction
Tkinter
 – for file selection dialog

Installation
Clone the repository:
    git clone https://github.com/revensonangela-stack/resume-analyzer.git
cd resume-analyzer


Create a virtual environment (optional but recommended):

python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows


Install dependencies:
pip install PyPDF2 python-docx

Usage
Run the main script:
python main.py


A file dialog will open to select your resume file (TXT, PDF, DOCX).
Then select the job description file (TXT, PDF, DOCX).

The program will output:

📄 Resume Analysis Report
-----------------------------------
Skill Match: 75%
Matched Skills: python, git, docker
Missing Skills: flask, ci/cd

💡 Suggestions:
- Consider adding experience with flask.
- Consider adding experience with ci/cd.

How It Works

Reads resume and job description files and extracts the text.
Uses a predefined common skills list for matching.
Finds intersection between resume skills and job description skills → matched skills
Calculates missing skills → skills present in JD but not in resume
Computes skill match percentage
Generates suggestions based on missing skills

Common Skills List
The analyzer currently includes a comprehensive list of skills including:
Programming languages: python, java, javascript, c++, c#, r, go, php, typescript
Frameworks & Web: flask, django, react, angular, node.js, rest api, graphql
Databases: sql, mysql, postgresql, mongodb, oracle, sqlite, redis
DevOps & Cloud: git, docker, kubernetes, aws, azure, gcp, ci/cd
Testing & Automation: selenium, pytest, unittest, junit, cucumber, postman, playwright
Data & ML: pandas, numpy, scikit-learn, tensorflow, keras, pytorch, matplotlib, seaborn
Others: linux, bash, shell scripting, oop, problem solving, agile, teamwork, communication

You can expand this list based on your target roles.

Contributing
Fork the repository
Make your changes
Submit a pull request
Suggestions welcome for improving skill detection, adding more file formats, or enhancing the UI.

License
This project is MIT licensed – feel free to use it for your portfolio or job preparation.