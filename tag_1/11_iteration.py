"""
Iteration über Listen
for-loop: Sammlungsorierter Loop
"""

ports = [80, 443, 232, 4242]
for port in ports:
    print("Port =>", port)


# Filtern einer Liste
ports = [80, 443, 232, 4242, 232, 14424, 2323, 80]
valid_ports = [80, 443]
filtered_ports = []

for port in ports:
    if port in valid_ports:
        filtered_ports.append(port)

# [80, 443, 80]
print("filtered ports:", filtered_ports)


# Zwei Listen an Index
students = ["Bob", "Alice", "Grumpy"]
grades = [1, 2, 4]

# Bob: 1
# Alice: 2
# Grumpy: 4
i = 0
for student in students:
    print(student, grades[i])
    i += 1

# Pythonische Variante: enumerate (wenn der Index benötigt wird)
for index, student in enumerate(students):
    print(student, grades[index])

enum_objekt = enumerate(students)  # Iterator, Iteratoren verbrauchen sich
print(list(enum_objekt))

# break
values = ["a1", "dk2", "skjfsljl3"]  # Abbruch oder print bei Substring 2
for value in values:
    if int(value[-1]) == 2:
        print("2 Wurde gefunden")
        break  # nur die aktuelle Iteration wird verlassen!


# continue
for i in [2, 3, 4, 5]:
    if i % 2 == 0:
        print("i**2:", i**2)
        continue  # sprint zum nächsten Element
    print(i)
