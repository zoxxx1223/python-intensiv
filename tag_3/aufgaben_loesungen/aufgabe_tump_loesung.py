from pathlib import Path

FILE_NAME = Path(__file__).parent / "trump_speeches.txt"
STRIP_CHARS = '.,;[]-#”“?!"'
MODI = ["SEN", "WORD", "TOP"]


file = open(FILE_NAME, "r", encoding="utf-8")
content = file.read()
file.close()
print(content[:20])

choose_modus = input("Wähle Modus: SEN, WORD, TOP: ")
choose_modus = choose_modus.split()  # SEN America

if choose_modus[0] not in MODI:
    print("Dieser Mode existiert leider nicht. Programmabruch")

elif choose_modus[0] == "SEN":
    search = choose_modus[1]

    # String nach Punkt splitten
    sentences = content.split(".")

    # über die Liste iterieren
    for sentence in sentences:
        # jeden Satz splitten und prüfen, ob Suchwort (search) enthalten ist
        if search in sentence.split():
            # Satz vorne und hinten von Steuerzeichen befreien und print
            print("=> ", sentence.strip())

elif choose_modus[0] == "WORD":
    search_word = choose_modus[1].lower()
    word_list: set = set()

    # content mit split() bei Leerzeichen trennen und in Worte zerlegen
    for word in content.split():
        # Jedes Word von Punkten und Zeichen befreien
        word = word.strip(STRIP_CHARS).replace(",", "")

        # Wort ad hoc in Liste in Kleinbuchstaben wandeln
        # und vergleichen
        if search_word in word.lower():
            # wenn es nicht schon in der Liste ist, in die Liste einfügen
            # Hinweis: wenn wir mit Set arbeiten würden (Menge), könnte man
            # sich diesen Schritt sparen
            word_list.add(word)

    print("Wortliste:")
    for word in word_list:
        print(f"=> {word}")

elif choose_modus[0] == "TOP":
    final_list = {}
    for word in content.split():
        word = word.strip(STRIP_CHARS).replace(",", "").lower()

        if len(word) > 5:
            if word in final_list:
                final_list[word] += 1
            else:
                final_list[word] = 1

    final_list = sorted(final_list.items(), key=lambda x: x[1], reverse=True)[0:20]
    print(final_list)

print("Thank you for using me!")
