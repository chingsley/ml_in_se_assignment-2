from openai import OpenAI
import os

DEEPSEEK_API_KEY = os.environ["DEEPSEEK_API_KEY"]


class Deepseek:

    def __init__(
        self,
        api_key=DEEPSEEK_API_KEY,
        base_url="https://api.deepseek.com",
    ):
        self.api_key = api_key
        self.base_url = base_url
        self.client = OpenAI(api_key, base_url)

    def prompt(self, prompt):
        response = self.client.chat.completions.create(
            model="deepseek-chat",
            messages=[
                {
                    "role": "system",
                    "content": "You are a senior software and a machine learning",
                },
                {"role": "user", "content": prompt},
            ],
            stream=False,
        )
        return response.choices[0].message.content
