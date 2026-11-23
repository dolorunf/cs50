user = input("Input expression: ")
given = user.split()
# print(user.split())
if len(given) != 3:
    print("Invalid expression")
else:
    try:
        x, y, z = user.split()
        x = int(x)
        z = int(z)
# print(x)
# print(y)
# print(z)
        if y == "-":
            print(f"answer: {x - z:.1f}")
        elif y == "+":
            print(f"answer: {x + z:.1f}")
        elif y == "*":
            print(f"answer: {x * z:.1f}")
        elif y == "/":
            print(f"answer: {x / z:.1f}")
        elif y == "%":
            print(f"answer: {x % z:.1f}")
        else:
            # raise ValueError("input a valid operator")
            print("Input something valid")
    except ValueError:
        print("Not an int")
    except ZeroDivisionError:
        print("Cannot divide by zero")


# def calculate_total(prices):
#     # prices = [2, 3, 4, 5, 6]
#     total = sum(prices)
#     return total


# prices = [2, 3, 4, 5, 6]
# print(calculate_total(prices))