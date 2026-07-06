
received = [120, 95, 180, 75]
sent = [100, 110, 180, 90]

for index, value in enumerate(received):
    if value > sent[index]:
        print("Minute", index + 1, ": mehr empfangen")
    elif value < sent[index]:
        print("Minute", index + 1, ": mehr gesendet")
    else:
        print("Minute", index + 1, ": gleich viele")
