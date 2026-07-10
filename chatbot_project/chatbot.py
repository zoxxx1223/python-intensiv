"""
Chatbot Klasse für OpenAI Chatbot

messages = [
    System-Message: Initiale Verhalten des Chatbots (Openai Chats)
    User-Message: User Anfrage
    Assistant-Message: Chatbot Antwort
    User-Message: User Anfrage
    Assistant-Message: Chatbot Antwort
]

abc = abstract BaseClasses
"""

from enum import StrEnum
from typing import Protocol

from openai import APIError, OpenAI


class ChatbotError(Exception):
    pass


class Role(StrEnum):
    """Rollen für die Messages-Liste."""

    SYSTEM = "system"
    USER = "user"
    ASSISTANT = "assistant"


class Chatbot(Protocol):
    """Gemeinsames Interface für alle Chatbot Klassen."""

    def talk(self, prompt: str) -> str:
        """Sendet einen Prompt an Chatbot."""
        ...


class OpenAIChatbot:
    """Einfacher Chatbot für das  Openai SDK."""

    def __init__(self, model: str, system_prompt: str):
        self.model = model
        self.system_prompt = system_prompt
        self.client = OpenAI()
        # in dieser Liste werden alle Nachrichten des gesamten Chat-Verlaufs
        # gespeichert
        self.messages = [
            {"role": Role.SYSTEM, "content": self.system_prompt},
        ]

    def _call_chatbot(self) -> str:
        try:
            response = self.client.chat.completions.create(
                model=self.model, messages=self.messages
            )
            content = response.choices[0].message.content
        except APIError as e:
            raise ChatbotError(f"Fehler bei der Kommunikation mit dem Bot: {e}")

        return content

    def talk(self, prompt: str) -> str:
        # Aufgabe: wenn prompot leer, raise Chatbot Error
        if not prompt.strip():
            raise ChatbotError("Chatbot Prompt darf nicht leer sein!")

        self.messages.append(
            {
                "role": Role.USER,
                "content": prompt,
            },
        )
        answer = self._call_chatbot()

        if answer is None:
            raise ChatbotError("Chatbot Antwort war leer")

        self.messages.append(
            {
                "role": Role.ASSISTANT,
                "content": answer,
            },
        )
        return answer
