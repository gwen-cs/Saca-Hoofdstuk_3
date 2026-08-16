agenda_punten = {
    1   :   "Add todo",
    2   :   "remove todo" ,
    3   :   "list todo" ,
    9   :   "exit"
}

def add_todo():
    item = input("Geef item dat je nog moet doen ?: ")

    todo_list.append(item)



def remove_todo():
    number = int(input("Welk item wil je dat ik wis?").strip())

    for i, do in enumerate (todo_list):
        if (i == number) :
            todo_list.remove(do)
            break

def list_todo():
    for i, do in enumerate (todo_list):
        print(f"{i} - {do}")


for index, agenda in agenda_punten.items():
    print(f"{index} - {agenda}")

state = int(input("Enter a number?: "))

todo_list = ["fietsen", "vissen"]

while state != 9:

    if (state == 1):
        add_todo()

    if (state == 2):
        remove_todo ()

    if (state == 3):
        list_todo()

    state = int(input("Enter a number?: "))







