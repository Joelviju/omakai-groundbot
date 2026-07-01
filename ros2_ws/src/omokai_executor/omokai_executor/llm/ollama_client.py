import requests

from .prompt import SYSTEM_PROMPT


class OllamaClient:
    """
    Thin wrapper around the local Ollama API.
    """

    def __init__(
        self,
        model: str = "mistral",
        host: str = "http://127.0.0.1:11434",
    ):

        self.model = model
        self.url = f"{host}/api/chat"

    def generate(self, user_prompt: str) -> str:
        """
        Sends a prompt to Ollama and returns the raw response text.
        """

        response = requests.post(

            self.url,

            json={

                "model": self.model,

                "stream": False,

                "messages": [

                    {
                        "role": "system",
                        "content": SYSTEM_PROMPT,
                    },

                    {
                        "role": "user",
                        "content": user_prompt,
                    },

                ],

            },

            timeout=120,

        )

        response.raise_for_status()

        data = response.json()

        return data["message"]["content"].strip()