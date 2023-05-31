import PyPDF2
import docx


def read_files(file_paths):
    files = file_paths.split(",")  # Split file paths by comma

    for file_path in files:
        file_extension = file_path.split(".")[-1].lower()

        if file_extension == "pdf":
            read_pdf(file_path)
        elif file_extension == "docx":
            read_docx(file_path)
        elif file_extension == "txt":
            read_text(file_path)
        else:
            print(f"Unsupported file type for file: {file_path}")


def read_pdf(file_path):
    try:
        with open(file_path, "rb") as file:
            pdf_reader = PyPDF2.PdfReader(file)
            text = ""
            for page in pdf_reader.pages:
                text += page.extract_text()
            print(f"Contents of PDF file: {file_path}\n{text}")
    except FileNotFoundError:
        print(f"File not found: {file_path}")


def read_docx(file_path):
    try:
        doc = docx.Document(file_path)
        text = ""
        for paragraph in doc.paragraphs:
            text += paragraph.text + "\n"
        print(f"Contents of DOCX file: {file_path}\n{text}")
    except FileNotFoundError:
        print(f"File not found: {file_path}")


def read_text(file_path):
    try:
        with open(file_path, "r") as file:
            text = file.read()
        print(f"Contents of TXT file: {file_path}\n{text}")
    except FileNotFoundError:
        print(f"File not found: {file_path}")


# Usage example
file_paths = input("Enter file path(s), separated by comma: ")
read_files(file_paths)
