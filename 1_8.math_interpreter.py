te_berekenen = input("Kan je me iets ingeven dat ik moet berekenen? ")

x, y, z = te_berekenen.split(" ")

x = int(x)
z = int(z)

match y:
    case "+":
        result = x + z
    case "-":
        result = x - z
    case "*":
        result = x * z
    case "/":
        result = x / z

print(f"{float(result):.1f}")
