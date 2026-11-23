import json

expenses = []  # to store multiple expenses


def add_expense():
    amount = int(input("Enter amount: "))
    if amount <= 0:
        print("Amount must be greater than 0")
        return
    category = input("Enter category: ").title().strip()
    if category == "":
        print("Category cannot be empty")
        return    
    description = input("Enter description: ")
    if description == "":
        print("Description cannot be empty")
        return
    acct = {
        "amount": amount,
        "category": category,
        "description": description    
    }
    expenses.append(acct)  # to add my new expense to my current expenses list


def view_expense():
    for number, expense in enumerate(expenses, start=1):
        print(f"{number}.{expense}")
        

def show_total():
    total = 0
    for i in expenses:
        total = total + i["amount"]   # to calculate the value stored under the amount in the expense dictionary
    print(f"The amount spent is {total}")


def show_spending():
    spending = {}   # i create a new dictionary to hold my category and amt 
    for i in expenses:
        if i["category"] in spending:  # to check if the category already exist inmy spending dictionary
            spending[i["category"]] = spending[i["category"]] + i["amount"]
        else:
            spending[i["category"]] = i["amount"]
    number = 1
    categories = []
    for category in spending:
        print(str(number) + ".", category) 
        categories.append(category)
        number = number + 1
    category = int(input("Which category do you want to calculate? "))
    if category <= 0 or category > len(categories):
        print("Category not found")
    else:
        category = category - 1
        category_name = categories[category]
        print(f"You spent {spending[category_name]} on {category_name}")


def delete_expense():
    for i in expenses:
        print(i)       
    delete = int(input("What number do you want to delete? "))
    if delete <= 0 or delete > len(expenses):
        print("Error")
    else:
        delete_number = delete
        delete = delete - 1  # i used dis since python list start counting from 0 sowith the -1 it will get the  correct item to delete for me
        del expenses[delete]  # to delete the expense at this exact position in the list
        print(f"Expense {delete_number} was deleted")
    

def save_json(expenses):  # i import this function to save my expenses
    with open('expense.json', 'w') as file:
        json.dump(expenses, file, indent=2)


def load_json():
    try:
        with open('expense.json', 'r') as file:
            data = json.load(file)  # to take the json data from the file and converts it back to python data 
            return data
    except FileNotFoundError:
        return []


def show_menu():    
    print("======= EXPENSE TRACKER =======")
    print("1. Add expense")
    print("2. View expense")
    print("3. Show total")
    print("4. Show spending by category")
    print("5. Delete expense")
    print("6. Exit")


expenses = load_json()

user = 0
while user != 6:
    show_menu()
    try:
        user = int(input("Choose an option: "))
        if user == 1:
            add_expense()
            save_json(expenses)
        elif user == 2:
            view_expense()
        elif user == 3:
            show_total()
        elif user == 4:
            show_spending()
        elif user == 5:
            delete_expense()
            save_json(expenses)        
        elif user == 6:
            print("Glad you were here!")
        else:
            print("input a valid option")
    except ValueError:
        print("Invalid input")


