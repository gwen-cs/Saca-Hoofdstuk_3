camelCase = input("Geef een woord in camelCase in zodat ik heet kan omzetten naar snake_case?: ")

te_verwerken = ""

for char in camelCase:

    if char.isupper():
        te_verwerken +="_" + char.lower()
    else :
        te_verwerken += char

print ("snake_case: ", te_verwerken)