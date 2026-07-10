# from chatbot import OpenAIChatbot
# bot = OpenAIChatbot()
# response = bot.talk("bla blubb")
from dotenv import load_dotenv
from chatbot import OpenAIChatbot, Chatbot, ChatbotError
import os


def run_chat(chatbot: Chatbot) -> None:
    """Startet eine Unterhaltung mit dem Chatbot."""
    while True:
        prompt = input("Du: ")
        if prompt in ["exit", "quit"]:
            print("Good bye...")
            break
        try:
            answer = chatbot.talk(prompt=prompt)
        except ChatbotError as e:
            answer = "ES kam keine Antwort..."

        print("Answer:", answer)


def main():
    load_dotenv()  # sucht nach .env -Datei im Root-Verzeichnis
    system_prompt = os.getenv("SYSTEM_PROMPT", "Default System Prompt")

    chatbot = OpenAIChatbot(
        model="gpt-4o-mini",
        system_prompt=system_prompt,
    )

    run_chat(chatbot=chatbot)


if __name__ == "__main__":
    main()
