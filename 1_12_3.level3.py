from aa_data import landen_data

def geef_naam(item):
    return item["land"]

def geef_hoofdstad(item):
    return item["hoofdstad"]

def geef_bevolking(item):
    return item["bevolking"]

gesorteerd_op_naam = sorted(landen_data, key=geef_naam)
gesorteerd_op_hoofdstad = sorted (landen_data, key=geef_hoofdstad)
gesorteerd_op_bevolking = sorted(landen_data, key= geef_bevolking, reverse=True)

top_10_bevolking = gesorteerd_op_bevolking[:10]

print("--- TOP 10 MEEST BRVOLKTE LANDEN ---")
for item in top_10_bevolking:
    print(f"{item['land']} : {item['bevolking']:,} inwoners")