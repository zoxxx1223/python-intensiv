eingabe = input("Bitte gebe ein gültiges Wort ein: ")

if " " in eingabe or eingabe.find("A") < 1 or len(eingabe) < 3:
    print("Ihre Eingabe war: ", eingabe)
    print("Ihre Eingabe ist leider falsch.")
else:
    print("Ihre Eingabe ist korrekt.")

print(eingabe.find("A"))  # 2



