import os
from openai import OpenAI


class ChatAgent:
    def __init__(self):
        self.client = OpenAI(
            api_key=os.getenv("OPENAI_API_KEY")
        )

        self.system_prompt = (
            "Tu es un responsable relation client professionnel, "
            "courtois, clair et orienté solution. "
            "Tu aides les clients concernant leurs commandes, "
            "retours, remboursements et problèmes de livraison."
        )

    def reply(self, message: str, client_id: str | None = None) -> str:
        response = self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": self.system_prompt},
                {"role": "user", "content": message},
            ],
            temperature=0.3,
        )

        return response.choices[0].message.content

