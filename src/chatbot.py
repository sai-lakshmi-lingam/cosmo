import requests
from retrieval import retrieve
from config import MODEL, OLLAMA_URL
from prompts import SYSTEM_PROMPT

def start_chat():
    print("Starting Cosmo...\n")

    history = []

    while True:

        try:
            prompt = input("Ask Cosmo something ('exit' to quit): ")

            if prompt.lower() == "exit":
                print("Goodbye!")
                break
            history.append(f"User: {prompt}") #new line

            documents = retrieve(prompt)
            context = "\n\n".join(documents)
            print("\n========== Retrieved Context ==========")
            print(f"Retrieved {len(documents)} document(s).")
            print(context)
            print("=======================================\n")

            conversation = "\n".join(history[:-1]) #nothing if no previous replies

            full_prompt = f"""
            {SYSTEM_PROMPT}

            Previous Conversation:
            {conversation}

            Retrieved Context:
            {context}

            Current Question:
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
                },
                timeout=300
            )
            print("Response received!")
            print(response.status_code)

            response.raise_for_status()

            answer = response.json()["response"]
            
            history.append(f"Cosmo: {answer}") #new line

            print("\nCosmo:")
            print(answer)
            print()
        except Exception as e:
            print(f"Error: {e}")