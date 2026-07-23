from sentence_transformers import SentenceTransformer

model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

text = "Glass skin focuses on hydration."

embedding = model.encode(text)

print(len(embedding))