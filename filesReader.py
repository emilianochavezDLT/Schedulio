import PyPDF2
import docx


def read_files(file_path):
    files = file_path.split(",")  # Split file path by comma to handle multiple files

    for file in files:
        file_extension = file.split(".")[-1].lower()

        if file_extension == "pdf":
            read_pdf(file)
        elif file_extension == "docx":
            read_docx(file)
        elif file_extension == "txt":
            read_text(file)
        else:
            print(f"Unsupported file type for file: {file}")


def read_pdf(file_path):
    try:
        with open(file_path, "rb") as file:
            pdf_reader = PyPDF2.PdfReader(file)
            text = ""
            for page in pdf_reader.pages:
                text += page.extract_text()
            return text
    except FileNotFoundError:
        print(f"File not found: {file_path}")


def read_docx(file_path):
    try:
        doc = docx.Document(file_path)
        text = ""
        for paragraph in doc.paragraphs:
            text += paragraph.text + "\n"
        return text
    except FileNotFoundError:
        print(f"File not found: {file_path}")


def read_text(file_path):
    try:
        with open(file_path, "r") as file:
            text = file.read()
        return text
    except FileNotFoundError:
        print(f"File not found: {file_path}")


# Usage example
file_path = input("Enter file path(s), separated by comma: ")
read_files(file_path)
