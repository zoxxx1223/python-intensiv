blockbelegung = input("Bitte geben Sie die Blockbelegung ein: ")

first_index = blockbelegung.find("1")

if first_index >= 0 and blockbelegung.find("01", first_index) >= 0:
    print("Datei ist fragmentiert.")
else:
    print("Datei ist zusammenhängend gespeichert.")
