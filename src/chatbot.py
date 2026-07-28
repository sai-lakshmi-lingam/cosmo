import requests
from retrieval import retrieve
from config import MODEL, OLLAMA_URL
from prompts import SYSTEM_PROMPT

def ask_cosmo(prompt, history):

    """
    Retrieves relevant documents, builds the prompt,
    sends it to Ollama, and returns Cosmo's response.
    """

    documents = retrieve(prompt)
    context = "\n\n".join(documents)

    print("\n========== Retrieved Context ==========")
    print(f"Retrieved {len(documents)} document(s).")
    print(context)
    print("=======================================\n")

    conversation = "\n".join(history[:-1])

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

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": MODEL,
            "prompt": full_prompt,
            "stream": False
        },
        timeout=300
    )

    response.raise_for_status()

    return response.json()["response"]

def start_chat():
    print("Starting Cosmo...\n")

    history = []

    while True:

        try:
            prompt = input("Ask Cosmo something ('exit' to quit): ")

            if prompt.lower() == "exit":
                print("Goodbye!")
                break

            history.append(f"User: {prompt}")

            answer = ask_cosmo(prompt, history)

            history.append(f"Cosmo: {answer}")

            print("\nCosmo:")
            print(answer)
            print()

        except Exception as e:
            print(f"Error: {e}")