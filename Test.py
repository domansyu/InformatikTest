import random

def zahlenratespiel():
    geheimzahl = random.randint(1, 100)
    versuche = 0

    print("Ich habe mir eine Zahl zwischen 1 und 100 ausgedacht.")
    print("Kannst du sie erraten?")

    while True:
        tipp = input("Dein Tipp: ")

        # Prüfen, ob die Eingabe eine Zahl ist
        if not tipp.isdigit():
            print("Bitte gib eine gültige Zahl ein.")
            continue

        tipp = int(tipp)
        versuche += 1

        if tipp < geheimzahl:
            print("Zu klein!")
        elif tipp > geheimzahl:
            print("Zu groß!")
        else:
            print(f"Richtig! Du hast {versuche} Versuche gebraucht.")
            break

zahlenratespiel()
