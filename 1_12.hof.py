"""
#1 Explain the difference between map, filter, and reduce.

antwoord_1_a = "map transformeert elk element Reduce "
antwoord_1_b = "Selecteert elk element op basis van voorwaarden"
antwoord_1_c = "combineert alle elementen tot een enkel resultaat"

#2 Explain the difference between higher order function, closure and decorator

countries = ["Belgium", "Netherlands", "France", "Germany"]

uppercase_countries = list(map(str, countries))

print(uppercase_countries)

countries = ["Finland", "Belgium", "Germany", "Netherlands", "Poland", "France"]

# Call-functie om te controleren of 'land' NIET in de naam zit
def no_land(country):
    return "land" not in country.lower()

# Gebruik filter om deze landen eruit te filteren
filtered_countries = list(filter(no_land, countries))

print(filtered_countries)

"""
from functools import reduce

landen = ["Estonia", "Finland", "Sweden", "Denmark", "Norway", "Iceland"]


def verbind_landen(acc, land):
    # Als het de laatste plaats in de lijst is, voeg ", and " toe
    if land == landen[-1]:
        return f"{acc}, and {land}"
    # Voor de overige landen, voeg simpelweg een komma en spatie toe
    else:
        return f"{acc}, {land}"


# Gebruik reduce om de zin op te bouwen en voeg het slotstuk toe
zin = reduce(verbind_landen, landen) + " are north European countries"

print(zin)