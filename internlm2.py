from langchain.llms.openai import OpenAI
import requests

class CustomOpenAI(OpenAI):
    def __init__(self, deployment_url: str, api_key: str = ""):
        super().__init__(api_key=api_key)
        self.deployment_url = deployment_url

    def _call(self, prompt, stop=None):
        headers = {"Authorization": f"Bearer {self.api_key}"}
        response = requests.post(
            self.deployment_url,
            headers=headers,
            json={
                "prompt": prompt,
                "max_tokens": self.max_tokens,
                "n": self.n,
                "stop": stop,
                "temperature": self.temperature,
            },
        )
        response.raise_for_status()
        return response.json()


