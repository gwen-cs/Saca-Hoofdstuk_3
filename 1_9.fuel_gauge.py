brandstof = input("Hoeveel brandstof zit er nog in de tank in 'breuk met spaties'?: ")

a, b, c = brandstof.split(" ")

while a > c :
    brandstof = input("Fout! Geef een geldige breuk: ")

    a, b, c = brandstof.split(" ")

    a = int(a)
    c = int(c)

a = int(a)
c = int(c)

procent = (a / c) * 100

if procent < 1 :
    print("Tank is leeg!")

elif procent > 99 :
    print("Tank is volledig vol!")

else:
    print(f"Er is nog {procent:.2f} % in de tank!")