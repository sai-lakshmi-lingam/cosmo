import chromadb
from config import DATABASE, TOP_RESULTS

client = chromadb.PersistentClient(path=DATABASE)

collection = client.get_collection(name="cosmo")

def retrieve(query):
    results = collection.query(
        query_texts=[query],
        n_results=TOP_RESULTS
    )

    print("IDS:")
    print(results["ids"])
    
    print("\nDISTANCES:")
    print(results["distances"])

    return results["documents"][0]