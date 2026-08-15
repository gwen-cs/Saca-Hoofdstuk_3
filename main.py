from functools import reduce

# dit is commentaar
"""
boodschap = "Hello-Wold"
print(boodschap)

name = input("What's your name?: ")
print ("hello", end=" ")
print (name)

print('hello, "friend"')

name = input("What's your name?: ")
print (f"your name is, {name} ")

name = input("What's your name?: ")
name = name.strip()
print(f"Hello {name}")
name = name.title()
print(f"Hello {name}")

name = input("What's your name?: ")
name = name.strip().title()
print(f"Hello {name}")

name = input("What's your name?: ").strip().title()
print(f"Hello {name}")

x = int(input("what's x?: "))
y = int(input("What's y?: "))
z = x + y
print (z)
x = float(input("what's x?: "))
y = float(input("What's y?: "))
z = round(x / y)
print (f"{z:.2f}")
print (f"{z:,}")

in_stock = 7
purchase_cnt = int(input("How many items do you want to purchase? "))
purchase_allowed = in_stock - purchase_cnt >= 0
print(purchase_allowed)

in_stock = 7
purchase_cnt = input("How many items do you want to purchase? ")
purchase_allowed = in_stock - purchase_cnt >= 0
print(purchase_allowed)

students = ["Hermione", "Harry", "Ron"]
print(len(students))

students[1] = "Draco"
print(len(students))

current_index = 0
while current_index < len(students):
    print(students[current_index])
    current_index += 1

for student in students:
    print(student)

courses = ["saca", "Leh", "chaos", "ctf"]
scores = [20, 15, 5, 15]

for i in range(len(courses)):
    print(f"For the course: {courses[i]} i got a score of {scores[i]}/20")

scores_per_course = {
    "saca": 20,
    "Leh": 15,
    "caos": 5,
    "ctf": 15
}

for course in scores_per_course:
    print(course)
    print(scores_per_course[course]

t1 = ("apple", "mango")
print(type(t1))  # <class 'tuple'>

t2 = "banana", "cherry"
print(type(t2))  # <class 'tuple'>

t1 = ("apple", "mango")
t2 = ("apple", 3, 1.4)
t3 = ("apple", 3, 1.4, ("banana", 5))

print(len(t1))  # 2
print(len(t2))  # 3
print(len(t3))  # 4

t1 = (327, 419, 101, 667, 925, 225)
print(max(t1))
print(min(t1))
print(sum(t1))

t1 = ("apple", "banana", "cherry")
print("banana" in t1)
print("mango" in t1)

t1 = ("apple", "banana", "cherry", "durian")
print(t1[2])

def say_hello(name):
    print(f"Hello there, {name}!")

say_hello("Gwen")


def calc_disc_surface(radius):
    return radius * radius * 3.1415

print(calc_disc_surface(15))


"""
def say_hello(name):
    print(f"Hello there, {name}!")

def calc_disc_surface(radius):
    return radius * radius * 3.1415

if __name__ == "__main__":
    name = input("enter your name: ")
    say_hello(name)

    radius = float(input("enter the radius of the disc: "))
    surface = calc_disc_surface(radius)

    print(f"Surface area of the disc: {surface}")

from functools import reduce

numbers_str = ['1', '2', '3', '4', '5']  # iterable

def add_two_nums(x, y):
    return int(x) + int(y)

total = reduce(add_two_nums, numbers_str)
print(total)    # 15