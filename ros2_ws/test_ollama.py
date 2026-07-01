from omokai_executor.llm.ollama_client import OllamaClient

client = OllamaClient()

response = client.generate(
    "Patrol the warehouse twice."
)

print(response)