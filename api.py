from random import choice, shuffle

cards = ["paper", "scissors", "rock"]
use = choice(cards)
shuffle(cards)
print(cards)
print(use)
students = ["Aviana", "Quiana", "Jair", "Jun", "Joy"]
print("These are my students")
for number, student in enumerate(students, start=1):
    # print("These are my students")
    print(f"{number}. {student}")


# import requests
# response = requests.get("https://jsonplaceholder.typicode.com/todos/1")
# data = response.json()
# print(data)
# if data["completed"]:
#     print("Task completed")
# else:
#     print("Task not completed")
# # print(data["title"])
# print(data["completed"])

# import requests

# response = requests.get("https://jsonplaceholder.typicode.com/todos/1")
# content = response.json()
# print(response.text)
# print(content)
name = "Dammy"

assert name == "Dammy"

print("Welcome!")


def multiply(a, b):
    return a * b


assert multiply(4, 3) == 12
print("Test Passed")


def divide(a, b):
    return a / b


assert divide(10, 2) == 5
print("Test passed")
assert divide(20, 4) == 5
print("Test passed")
try:
    assert divide(4, 3) == 2
    print("Test passed")
except AssertionError:
    print("Mathematically it's not correct")

# names = []
# for i in range(3):
#     name = input("what's your name? ")
#     names.append(name)
# for name in names:
#     print(f"Hello, {name}!")


for i in range(1, 11):
    print(i)


let age = 20;

if (age >= 18) {
    console.log("You are an adult")
} else {
    consol.log("You are not an adult")
}


let number = -3;

if (number > 0) {
    console.log("Postive number")
} else {
    console.log("Not a postive number")
}

let age = 17;

if (age >= 18) {
    console.log("You can vote")
} else {
    console.log("You are not eligile")
}


let temperature = 25;

if (temperature > 30) {
    console.log("It is very hot")
} else if (temperature > 20) {
    console.log("The weather is warm")
} else {
    console.log("The weather is cold")
}

for (let i = 6; i <= 1; i--) {
    console.log(i);
}

for ( let i = 0; i <= 6; i++) {
    console.log("hello")
}

for (let i = 2; i <= 20; i += 2) {
    console.log(i)
}

for (let i = 1; i <= 5; i++) {
    if (i % 2 === 0) {
        console.log("Even")
    }else {
        console.log("Odd")
    }
}

for (let i = 10; i >= 1; i -= 2) {
    console.log(i)
}

for (let i = 6; i >= 1; i--) {
    console.log(i)
}


student = {
    "name": "Dammy",
    "age": 20,
    "Learning_python": True
}