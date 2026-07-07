MIN_NITROGEN = 0
MAX_NITROGEN = 100
OPTIMAL_MIN = 20
OPTIMAL_MAX = 40
EXIT_COMMANDS = ["exit", "ende", "quit"]

measurements = []

print("Willkommen beim Stickstoff-Messgerät 2000")
print("Kalkulieren Sie den Stickstoff Ihrer Zimmerpflanze!")

while True:
    user_input = input(
        f"Geben Sie den Stickstoffgehalt in % ein (oder {EXIT_COMMANDS} zum Beenden): "
    )

    if user_input.lower() in EXIT_COMMANDS:
        break

    if user_input.replace(".", "", 1).isdigit():
        value = float(user_input)

        if MIN_NITROGEN <= value <= MAX_NITROGEN:
            measurements.append(value)
        else:
            print(
                f"Ungültig. Bitte geben Sie einen Wert zwischen "
                f"{MIN_NITROGEN}% und {MAX_NITROGEN}% ein."
            )
    else:
        print("Das ist keine gültige Zahl. Bitte versuchen Sie es erneut.")

if measurements:
    average = sum(measurements) / len(measurements)
    print(f"Durchschnittlicher Stickstoffgehalt: {average:.2f}%")

    if OPTIMAL_MIN <= average <= OPTIMAL_MAX:
        print("Der Durchschnittswert liegt im optimalen Bereich.")
    else:
        print("Der Durchschnittswert liegt außerhalb des optimalen Bereichs.")
else:
    print("Keine gültigen Messwerte eingegeben.")
