from parser import parse_pdf
from chunker import chunk_text
from embedder import Embedder
from vector_store import VectorStore
from retriever import Retriever
from generator import build_prompt, generate

def main():
    # 1. parse
    print("Parsing..")
    text = parse_pdf("data/sample3.pdf")
    print(f"전체 문서 길이: {len(text)}")

    # 2. chunk
    print("Chunking..")
    chunks = chunk_text(text, chunk_size=500, overlap=100)
    print(f"청크 개수: {len(chunks)}")

    # 3. embed
    print("Embedding..")
    embedder = Embedder()
    embeddings = embedder.embed_documents(chunks)

    # 4. store
    print("Storing..")
    vector_store = VectorStore()
    vector_store.add(chunks, embeddings)

    # 5. retrieve
    retriever = Retriever(embedder, vector_store)
    while True:
        query = input("질문을 입력하세요 (quit): ")

        if query == 'quit':
            break

        print("Retrieving..")
        results = retriever.retrieve(query, top_k=3)

        documents = []

        for i, (document, score) in enumerate(results, start=1):
            print(f"===검색결과{i} (score={score:.4f})===")

            print(document[:300])

            documents.append(document)
        # 6. prompt
        print("Prompting..")
        prompt = build_prompt(query, documents)

        # 7. generate
        print("Generating..")
        answer = generate(prompt)
        print("Answer: ", answer)

if __name__ == "__main__":
    main()