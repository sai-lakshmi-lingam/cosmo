import requests

print("Starting program...")

prompt = input("Ask Cosmo something: ")

response = requests.post(
    "http://localhost:11434/api/generate",
    json={
        "model": "qwen3:8b",
        "prompt": prompt,
        "stream": False
    }
)

answer = response.json()["response"]

print("\nCosmo:")
print(answer)