import re
from pathlib import Path
from typing import Set
from PyPDF2 import PdfReader
from docx import Document

class UnsupportedFileTypeError(Exception):
    """Raised when an unsupported resume format is provided."""


# -----------------------------
# Define all possible common skills
# -----------------------------
COMMON_SKILLS = {
    # Programming Languages
    "python", "java", "javascript", "c++", "c#", "c", "ruby", "go", "php", "typescript", "r", "swift",
    
    # Web / Backend
    "html", "css", "flask", "django", "react", "angular", "node.js", "express", "rest api", "graphql",
    
    # Databases
    "sql", "mysql", "postgresql", "mongodb", "oracle", "sqlite", "redis", "cassandra", "firebase",
    
    # DevOps / Tools
    "git", "docker", "kubernetes", "aws", "azure", "gcp", "ci/cd", "jenkins", "terraform", "ansible",
    
    # Testing / QA
    "selenium", "pytest", "unittest", "junit", "cucumber", "postman", "playwright", "automation testing",
    
    # Data / ML / AI
    "pandas", "numpy", "scikit-learn", "tensorflow", "keras", "pytorch", "matplotlib", "seaborn",
    
    # Others
    "linux", "bash", "shell scripting", "restful api", "api", "oop", "object oriented programming",
    "problem solving", "agile", "scrum", "teamwork", "communication", "critical thinking",
    "leadership", "time management", "documentation", "debugging", "troubleshooting", "version control",
    "cloud", "microservices", "serverless", "html5", "css3", "bootstrap", "material ui"
}


def extract_text(file_path: str) -> str:
    """Extracts text from TXT, PDF, or DOCX files safely."""
    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")

    try:
        if path.suffix == ".txt":
            return _read_txt(path)
        elif path.suffix == ".pdf":
            return _read_pdf(path)
        elif path.suffix == ".docx":
            return _read_docx(path)
        else:
            raise UnsupportedFileTypeError(f"Unsupported file type: {path.suffix}")
    except Exception as exc:
        raise RuntimeError(f"Failed to extract text from {file_path}") from exc


def _read_txt(path: Path) -> str:
    with open(path, "r", encoding="utf-8") as file:
        return file.read().lower()


def _read_pdf(path: Path) -> str:
    reader = PdfReader(path)
    text = ""
    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text + " "
    return text.lower()


def _read_docx(path: Path) -> str:
    doc = Document(path)
    return " ".join(p.text for p in doc.paragraphs).lower()


def extract_skills(text: str) -> Set[str]:
    """
    Extract skills from text by checking against COMMON_SKILLS.
    Returns a set of matched skills.
    """
    text = text.lower()
    found_skills = set()
    for skill in COMMON_SKILLS:
        # Regex ensures exact match, including multi-word skills
        pattern = r"\b" + re.escape(skill) + r"\b"
        if re.search(pattern, text):
            found_skills.add(skill)
    return found_skills
