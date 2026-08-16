boodschappenlijstje = []

while True:

    try:
        invoer_boodschap = input("Wat dient er gehaald te worden in de winkel?: ").stripe().upper();
        boodschappenlijstje.append(invoer_boodschap)
    except EOFError:
        break
boodschappenlijstje.sort()

aantallen = {}

for boodschap in boodschappenlijstje :
    if boodschap in aantallen:
        aantallen[boodschap] +=1
    else :
        aantallen[boodschap] = 1

for boodschap, aantal in aantallen.items():
    print(f"{aantal} x {boodschap}")
