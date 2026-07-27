import chromadb
from pathlib import Path

client = chromadb.PersistentClient(path="./chroma_db")

try:
    client.delete_collection("cosmo")
except:
    pass

collection = client.get_or_create_collection(name="cosmo")

DATA_FOLDER = Path(__file__).parent.parent / "data"
txt_files = DATA_FOLDER.rglob("*.txt")

documents = []
ids = []

for i, file in enumerate(txt_files):

    text = file.read_text(encoding="utf-8")

    documents.append(text)

    ids.append(file.stem)

collection.add(
    documents=documents,
    ids=ids
)

print("Documents added.")