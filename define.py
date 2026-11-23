def greet():
    print("Hello, welcome to Python!")  # exercise 1


greet()


def say_goodbye():
    print("Goodbye!")  # exercise 2


say_goodbye()


def welcome(name):
    print("Welcome," + " " + name + "!")  # 3 function with parameters


welcome("David")


def square(number):
    return number ** 2  # exercise 4 with parameter


print(square(4))


def multiply(a, b):
    return a * b 


print(multiply(6, 5))  # exercise 5 using parameters


def maximum(a, b):
    return max(a, b)


print(maximum(7, 10))  # using return 


def is_even(number):
    return number % 2 == 0


print(is_even(8))


def full_name(first, middle, last):
    print(first, middle, last)


full_name("Damilola", "Ayomitide", "Olorunfemi")


def check_age(age):
    if age >= 18:
        return "Adult"
    else:
        return "Minor"


print(check_age(20))


def grade(score):
    if score >= 70 or score == 100:
        return "A"
    elif score >= 60 or score == 69:
        return "B"
    elif score >= 50 or score == 59:
        return "C"
    else:
        return "Fail"


print(grade(100))    


def calculator(a, b):
    return {
        "sum": a + b,
        "difference": a - b,
        "product": a * b
    }


print(calculator(8, 2))


def temperature(celsius):
    fahrenheit = (celsius * 9/5) + 32
    celsius = fahrenheit
    return fahrenheit


print(temperature(25))


def shout(text):
    text.upper() == "hello"
    return text.upper()


print(shout("hello"))


def count_letters(word):
    return len(word)


print(count_letters("Python"))


def reverse_word(word):
    return word[::-1]


print(reverse_word("Python"))


def safe_divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    else:
        return a / b


print(safe_divide(4, 2))


def password_check(password):
    # password = input("Enter your password: ")
    if len(password) >= 8:
        return "Strong Password"
    else:
        return "Weak Password"

# print(password_check())


print(password_check("hello6776"))


def shopping_total(price, quantity):
    total_cost = price * quantity
    return total_cost


print(shopping_total(1500, 4))


def largest_of_three(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c


print(largest_of_three(12, 8, 20))


def student_result(score, attendance):
    if score >= 70 and attendance >= 80:
        return "Excellent"
    if score >= 50:
        return "Pass"
    else:
        return "Fail"


print(student_result(85, 90))


def get_guess():
    guess = int(input("Enter a guess: "))
    return guess


def main():
    guess = get_guess()

    if guess == 45:
        print("WOW, you got it right!")
    else:
        print("Oops, try again")


main()