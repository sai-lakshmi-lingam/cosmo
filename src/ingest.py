import chromadb

client = chromadb.PersistentClient(path="./chroma_db")

collection = client.create_collection(
    name="cosmo"
)

collection.add(
    documents=[
        "Glass skin emphasizes hydration.",
        "The clean girl aesthetic focuses on natural makeup."
    ],
    ids=[
        "1",
        "2"
    ]
)

print("Documents added.")