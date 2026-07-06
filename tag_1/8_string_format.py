"""
String formatieren: format() und f-String
"""
city = "Hamburg"
print(f"Das ist ein String mit {city} Buchstaben: {len(city)}")

# Runden auf 2 Nachkommastellen
points = 19
total = 22
print(f"Correct Answers: {points / total:.2f}") # Float gerundet
print(f"Correct Answers: {points / total:.2%}") # prozentual

# Raw-String
raw_string = r"c:\home\hello"