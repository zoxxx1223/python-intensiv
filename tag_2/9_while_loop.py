"""
While: Bedingungskontrollierte Kopfschleife
Wird immer nur dann genutzt, wenn man nicht weiß, wie lange eine Schleife läuft

while <BEDINGUNG>:
    ...
"""

x = 5
while x > 0:
    print(f"{x}")
    x -= 1
else:
    print("Loop beendet")


while True:
    ui = input("> ")
    if ui.lower() in ["exit", "quit", "bye"]:
        print("Good bye...")
        break


# Zahlenratespiel
# Zufallszahl errechnen (mit random.randint), zb. 4
# maximale Rateversuche: 4
# whileloop
# pro Loop ein User Input. Ist user input nicht gleich der Zufallszahl
# leider falsch, bitte nochmal raten
# im Glück gehabt, du hast gewonnen!
# falls die Anzahl der Rateversuche >= der maximalen Rateversuche, Game over

import random

start = random.randint(1, 10)
