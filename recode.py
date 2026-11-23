import json

expenses = []


def save_json(expenses):
    with open('expense.json', 'w')as file:
        json.dump(expenses, file, indent=2)


def load_json():
    try:
        with open('expense.json', 'r')as file:           
            data = json.load(file)
            return data
    except FileNotFoundError:
        return []


def add_expense():
    amount = int(input("Enter Amount: "))
    if amount <= 0:
        print("Amount cannot be less or equal to zero")
        return
    category = input("Enter Category: ")
    if category == "":
        print("Category cannot be empty")
        return
    description = input("Enter Description")
    if description == "":
        print("Description cannot be empty")
        return
   
    acct = {
        "Amount": amount,
        "Category": category,
        "Description": description
}

    expenses.append(acct)


def view_expenses():
    for number, expense in enumerate(expenses, start=1):
        print(f"{number}. {expense}")


def show_total():
    total = 0
    total = total + i["amount"]
    print(f"Total money spent is {total}")


def show_spending():
    spending = {}
    for i in expenses:
        if i['category'] in spending:
            spending[i['category']] += i['amount']
        else:
            spending[i['category']] = i['amount']

    for item in spending.items():
        return spending
    pass


def delete_expense():  
    for i in expenses:
        print(i)
        delete = int(input("What number do you want to delete? "))
        if delete <= 0 or delete > len(expenses):
            print("Out of Range")
        else:
            delete_number = delete
            delete =- 1
            del expenses[delete]
            print(f"Expense {delete_number} has been deleted")


def show_menu():
    print("=====WELCOME=====")
    print("1. Add expense")
    print("2. view expenses")
    print("3. show total")
    print("4. show spending by category")
    print("5. delete expense")
    print("6. Exit")


expenses = load_json
user = 0
while user != 6:
    show_menu()
    try:
        user = int(input("Choose an Option: "))
        if user == 1:
            add_expense()
            save_json(expenses)
        elif user == 2:
            view_expenses()
        elif user == 3:
            show_total()
        elif user == 4:
            show_spending()
        elif user == 5:
            delete_expense()
        elif user == 6:
            print("Okay, Bye!")
        else:
            print("Pick within the range")
    except ValueError:
        print("Input something Valid")


if total == 0:
    return 0
return round((len / width)*100)

if total == 0:
    return 0
return round((len / width)* 100)

for index, balance in enumerate(balances):
    if balance < index:
        return index
return -1

for index, balance in enumerate(balances):
    if balance < index:
        return index
return -1

lis = list(map(lambda x: x.strip().lower(), normalize))
return lis

spending = {}
for i in expenses:
    if i['category'] in spending:
        spending[i['category']] += i['amount']
    else:
        spending[i['category']] = i['amount']

for item in spending.items:
    return spending

lis = list(map(lambda x: x.strip().lower(), normalize))
return lis

for index, balance in enumerate(balances):
    if balance < index:
        return index
return -1

def count_correct(questions, answers):
    score = 0
    for question, answer in zip(questions, answers):
        if answer == question['answer']:
            score += 1
    return score


        for task in tasks:
            if task.get("id") == tasks:
                return task
        return None

spending = {}
for i in expenses:
    if i['category'] in spending:
        spending[i['category']] += i['amount']
    else:
        spending[i['category']] = i['amount']

for item in spending.items:
    return spending


lis = list(map(lambda x: x.strip().lower(), normalize))
return lis

for task in tasks:
    if task.get('id') == tasks:
        return task
return None

total = 0
total = total + i['amount']
return total


score = 0
for question, answer in zip(questions, answers):
    if answer == question['answer']:
        score+=1
return score

for task in tasks:
    if task.get('id') == tasks:
        return task

return None


lis = list(map(lambda x: x.strip().lower(), normalize))
return lis


def show_spending():
    spending = {}
    for i in expenses:
        if i['category'] in spending:
            spending[i['category']] += i['amount']
        else:
            spending[i['amount']] = i['amount']

    for item in spending.items():
        return spending
score = 0
for question, answer in zip(questions, answers):
    if answer == question['answer']:
        score += 1
return score 

for book in books:
    if book == [completed]:
        return book

score = 0
for question, answer in zip(questions, answers):
    if answer == question['answer']:
        score += 1
return score

spending = {}
for i in expenses:
    if i['category'] in spending:
        spending[i['category']] += i['amount']
    else:
        spending[i['category']] = i['amount']
for item in spending.items():
    return spending

score = 0 
for answer in answers:
    for question in questions:
        if question['answers'] == answer:
            score += 1
    return score


if not products:
    return None

lowest = min(products, key=lambda product: (product["quantity"], product["id"]))

return lowest["id"]

balance = principal * (1 + rate) ** periods
return round(balance, 2)
