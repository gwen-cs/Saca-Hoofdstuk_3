from zoneinfo import reset_tzpath

zin = input("Kan je me een zin geven die een smily terug geeft?: ")

isSmily = ":)"
isCry = ":("

def faces (zin):
    if isSmily in zin:
        zin = zin.replace (":)","🙂")
    if isCry in zin:
        zin = zin.replace(":(", "🙁")

    return zin

print(faces(zin))