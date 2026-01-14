# Resume Analyzer & Skill Gap Finder

A Python tool that analyzes your **resume** against a **job description** and highlights **matched** and **missing skills**. Ideal for job seekers looking to optimize their resumes for specific roles.

---

## Features

- Supports **resume and job description files**: TXT, PDF, DOCX
- Identifies **matched skills** and **missing skills** based on a predefined skills list
- Calculates **skill match percentage**
- Provides **suggestions** to improve your resume

---

## How It Works

1. Extracts text from resume and job description files.
2. Compares the text against a **common skills list**.
3. Finds **skills present in both** → matched skills.
4. Finds **skills in the job description but missing in the resume** → missing skills.
5. Calculates **skill match percentage**.
6. Generates **actionable suggestions** to improve your resume.

---

## Installation

1. Clone the repository:

    git clone https://github.com/revensonangela-stack/resume-analyzer.git
    cd resume-analyzer

    Install dependencies:
    pip install PyPDF2 python-docx

    Usage
    Run the main program:
    python main.py
    Select your resume file (TXT, PDF, DOCX)

    Select the job description file (TXT, PDF, DOCX)

The program outputs:

📄 Resume Analysis Report
-----------------------------------
Skill Match: 75%
Matched Skills: python, git, docker
Missing Skills: flask, ci/cd

💡 Suggestions:
- Consider adding experience with flask.
- Consider adding experience with ci/cd.
Common Skills List
Programming Languages: python, java, javascript, c++, c#, php, typescript, r, go
Frameworks / Web: flask, django, react, angular, node.js, rest api, graphql
Databases: sql, mysql, postgresql, mongodb, oracle, sqlite, redis
DevOps / Cloud: git, docker, kubernetes, aws, azure, gcp, ci/cd
Testing / QA: selenium, pytest, unittest, junit, cucumber, postman, playwright
Data / ML: pandas, numpy, scikit-learn, tensorflow, keras, pytorch, matplotlib, seaborn
Other Skills: linux, bash, shell scripting, oop, problem solving, agile, teamwork, communication, debugging, troubleshooting, version control, documentation

(You can expand the list depending on the role.)

License
This project is licensed under the MIT License.