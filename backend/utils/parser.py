import textract

def extract_text_from_file(path: str) -> str:
    try:
        text = textract.process(path).decode("utf-8")
        return text
    except Exception as e:
        return f"Error extracting text: {str(e)}"
