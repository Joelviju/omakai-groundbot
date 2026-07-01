from .mission import Mission
from .llm.prompt import build_prompt
from .llm.ollama_client import OllamaClient
from .llm.parser import parse_mission


class MissionGenerator:
    """
    Generates a Mission using a local LLM (Ollama).
    """

    def __init__(self):

        self.client = OllamaClient()

    def generate(self, user_prompt: str) -> Mission:

        prompt = build_prompt(user_prompt)

        response = self.client.generate(prompt)

        mission = parse_mission(response)

        return mission