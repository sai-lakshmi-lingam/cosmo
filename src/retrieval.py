import chromadb

client = chromadb.PersistentClient(path="./chroma_db")

collection = client.get_collection(
    name="cosmo"
)

results = collection.query(
    query_texts=[
        "How do I get dewy skin?"
    ],
    n_results=2
)

print("Most relevant documents:\n")

for doc, distance in zip(
    results["documents"][0],
    results["distances"][0]
):
    print(f"- {doc}")
    print(f"  Distance: {distance:.3f}\n")