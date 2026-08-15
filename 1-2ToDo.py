agenda_punten = {
    1   :   "Add todo",
    2   :   "remove todo" ,
    3   :   "list todo" ,
    9   :   "exit"
}

for index, agenda in agenda_punten.items():
    print(f"{index} - {agenda}")

state = int(input("Enter a number?: "))


while state != 9:
    state = int(input("Enter a number?: "))