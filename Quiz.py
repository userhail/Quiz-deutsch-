print("Hallo, willkommen zum Quiz") 

name = input("geben sie ihren Namen ein ")

print(f"willkommen zum Quiz {name}")
punkte = 0

def richtig():
    global punkte
    print("Deine Antwort ist richtig")
    punkte += 1

def falsch():
    print("Deine Antwort ist Falsch")

Schwierigkeit = input("Schwierigkeitsgrad: normal oder schwer? ").strip().lower()

if Schwierigkeit == "normal":
    antwort = input("In welchem Kontinent liegt die Mongolei? ").strip().lower()

    if antwort == ("asien"):
        richtig()
        
    else:
       falsch()

    antwort = input("Wo wird die jetztige WM 2026 gespielt? Nenne den Kontinent ").strip().lower()

    if antwort in ["nordamerika", "amerika"]:
        richtig()
    else:
        falsch()

    antwort = input("Letzte Frage, was ist die Hauptstadt von Japan? ").strip().lower()

    if antwort in ["tokyo", "tokio"]:
        richtig()

    else:
        falsch()

elif Schwierigkeit == "schwer":
    antwort = input("Wie lautet das chemische Symbol für Gold? ").strip().lower()
    
    if antwort == "au":
        richtig()

    else: 
        falsch()

    antwort = input("Welches ist das kleinste Land in Asien? ").strip().lower()

    if antwort == "malediven":
        richtig()

    else:
        falsch()

    antwort = input("Nenne eine von den zwei beliebtesten Parteien in der USA. ").strip().lower()
    
    if antwort in ["demokratische partei", "demokraten", "republikaner", "republikanische partei"]:
        richtig()

    else:
        falsch()

else: 
    print("Ungültige Eingabe")

print(f"du hast {punkte} Punkt/e erreicht")