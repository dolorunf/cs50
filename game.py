# def recommend(game):
#     print("You might like", game)


# while True:
#     difficulty = input("Difficult or Casual? ").lower()
#     players = input("Multiplayer or Single player? ").lower()

#     if difficulty == "difficult" and players == "multiplayer":
#         recommend("Poker")
#     elif difficulty == "difficult" and players == "single player":
#         recommend("Klondike")
#     elif difficulty == "casual" and players == "multiplayer":
#         recommend("Heart")
#     elif difficulty == "casual" and players == "single player":
#         recommend("Clock")
#     else:
#         print("Enter a valid answer")


students = [
    {"name": "John", "age": 20},
    {"name": "Mary", "age": 22},
    {"name": "David", "age": 19}
]
for student in students:
    print(students)


def count_down(cups):  # Recursion function
    if cups <= 0:
        print("Done!")
        return
    print("Cup: " + str(cups))
    count_down(cups - 1)


count_down(3)