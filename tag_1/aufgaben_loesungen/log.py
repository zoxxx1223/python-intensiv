filename = input("Dateiname: ")

if len(filename) < 3:
    result = filename
elif filename.endswith("log"):
    result = filename + "1"
else:
    result = filename + "log"

print(result)