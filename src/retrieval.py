import chromadb
from config import DATABASE, TOP_RESULTS

client = chromadb.PersistentClient(path=DATABASE)

collection = client.get_collection(name="cosmo")

def retrieve(query):
    results = collection.query(
        query_texts=[query],
        n_results=TOP_RESULTS
    )

    return results["documents"][0]