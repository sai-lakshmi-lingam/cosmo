import requests
from retrieval import retrieve
from config import MODEL, OLLAMA_URL
from prompts import SYSTEM_PROMPT

def start_chat():
    print("Starting Cosmo...\n")

    while True:

        prompt = input("Ask Cosmo something ('exit' to quit): ")

        if prompt.lower() == "exit":
            print("Goodbye!")
            break

        documents = retrieve(prompt)
        context = "\n\n".join(documents)
        print("\nRetrieved Context:")
        print(context)
        print()
        
        full_prompt = f"""
        {SYSTEM_PROMPT}

        Use the following context to answer the question.

        Context:
        {context}

        Question:
        {prompt}

        Answer:
        """

        print("Sending prompt to Ollama...")

        response = requests.post(
            OLLAMA_URL,
            json={
                "model": MODEL,
                "prompt": full_prompt,
                "stream": False
            }
        )
        print("Response received!")
        print(response.status_code)

        answer = response.json()["response"]

        print("\nCosmo:")
        print(answer)
        print()