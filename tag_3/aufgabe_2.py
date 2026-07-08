from pathlib import Path

BASE_DIR = Path(__file__).parent.parent

while True:
    user_zeile = input("Bitte Zeile zum Speichern eingeben: ")

    if user_zeile.lower() in ["quit", "exit"]:
        break

    if user_zeile.strip() == "":
        print("Bitte etwas eingeben.")
        continue

    with open(BASE_DIR / "user.log", mode="a", encoding="utf-8") as f:
        f.write(f"{user_zeile}\n")
