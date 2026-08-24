# PDF 텍스트 추출

from pathlib import Path
from pypdf import PdfReader

def parse_pdf(file_path: str) -> str:
    reader = PdfReader(file_path)

    texts = []

    for page in reader.pages:
        text = page.extract_text()

        if text:
            texts.append(text)

    return "\n".join(texts)

if __name__ == "__main__":
    text = parse_pdf("rag-structure/data/sample.pdf")

    print(text)