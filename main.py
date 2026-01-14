from tkinter import Tk, filedialog

from analyzer.parser import extract_text, extract_skills, UnsupportedFileTypeError
from analyzer.matcher import match_skills
from analyzer.scorer import calculate_score
from analyzer.suggester import generate_suggestions


def select_file(title: str) -> str:
    """
    Opens a file explorer dialog and returns the selected file path.
    """
    root = Tk()
    root.withdraw()  # Hide the main tkinter window
    root.attributes("-topmost", True)

    file_path = filedialog.askopenfilename(
    title=title,
    filetypes=[
        ("All supported files", "*.txt *.pdf *.docx"),   # Show all relevant types together
        ("Text files", "*.txt"),
        ("PDF files", "*.pdf"),
        ("Word documents", "*.docx"),
        ("All files", "*.*")    # Optional: allow any file to be shown
        ]
    )   

    root.destroy()

    if not file_path:
        raise FileNotFoundError("No file selected.")

    return file_path


def main():
    try:
        print("📂 Please select your RESUME file")
        resume_path = select_file("Select Resume")

        print("📂 Please select the JOB DESCRIPTION file")
        jd_path = select_file("Select Job Description")

        # Extract text from files
        resume_text = extract_text(resume_path)
        jd_text = extract_text(jd_path)

        # Extract matched and missing skills dynamically
        resume_skills = extract_skills(resume_text)
        print(resume_skills)
        jd_skills = extract_skills(jd_text)
        print(jd_skills)

        results = match_skills(resume_skills, jd_skills)
        score = calculate_score(len(results["matched"]), len(jd_skills))
        suggestions = generate_suggestions(results["missing"])


        # Print analysis report
        print("\n📄 Resume Analysis Report")
        print("-" * 35)
        print(f"Skill Match: {score}%")
        print(f"Matched Skills: {', '.join(sorted(results['matched'])) or 'None'}")
        print(f"Missing Skills: {', '.join(sorted(results['missing'])) or 'None'}")

        if suggestions:
            print("\n💡 Suggestions:")
            for suggestion in suggestions:
                print("-", suggestion)

    except FileNotFoundError as err:
        print(f"❌ File selection error: {err}")
    except UnsupportedFileTypeError as err:
        print(f"❌ Unsupported file type: {err}")
    except RuntimeError as err:
        print(f"❌ Processing error: {err}")
    except Exception as err:
        print(f"❌ Unexpected error: {err}")


if __name__ == "__main__":
    main()
