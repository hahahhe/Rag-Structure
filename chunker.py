# 청킹

def chunk_text(text: str, chunk_size: int=500, overlap: int=100) -> list[str]:
    chunks = []

    start = 0
    while start < len(text):
        end = start + chunk_size
        chunk = text[start:end]
        chunks.append(chunk)
        start += chunk_size - overlap

    return chunks

if __name__ == "__main__":
    text = "ㄱㄴㄷㄹㅁㅂㅅㅇㅈㅊㅋㅌㅍㅎ가나다라마바사아자차카타파하"

    chunks = chunk_text(text, chunk_size=10, overlap=3)

    for chunk in chunks:
        print("--", chunk)