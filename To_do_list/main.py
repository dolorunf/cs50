tasks = []  # to add multiple tasks


def show_menu():
    print("-----------------------------")
    print("          WELCOME            ")
    print("-----------------------------")
    print("What would you like to do?")
    print("1. Add task")
    print("2. View tasks")
    print("3. Complete task")
    print("4. Edit task")
    print("5. Delete task")
    print("6. Filter tasks")
    print("7. Exit")


def add_task():
    ask = input("What task do you want to add? ").strip()
    if ask == "":
        print("Enter a Task")
    else:
        print(f"Task: {ask}")
        tasks.append({
            "task": ask,
            "completed": False
        })
   

def view_tasks():
    print("Here is a list of what we have")
    if not tasks:
        print("Tasks is empty")
    else:
        for number, task in enumerate(tasks, start=1):
            print(f"{number}. {task['task']}")


def complete_task():
    print("Okay Check")


def edit_task():
    view_tasks()
    if not tasks:
        print("Tasks is empty")
        return
    edit = int(input("Which task do you want to edit? "))
    if edit <= 0 or edit > len(tasks):
        print("Input a valid number")
    else:
        edit_number = edit
        edit = edit -1
        new_task = input("What is the new task? ")
        if new_task == "":
            print("Enter a task")
        else:
            tasks[edit] = new_task
            print(f"Task {edit_number} has been updated")


def delete_task():
    view_tasks()
    if not tasks:
        print("Tasks is empty")
        return
    delete = int(input("Which number do you want to delete? "))
    if delete <= 0 or delete > len(tasks):
        print("Number not avaialbe")
    else:
        delete_number = delete
        delete = delete -1
        del tasks[delete]
        print(f"Task {delete_number} was deleted")
  

def filter_tasks():
    print("Then filter")


user = 0

while user != 7:
    show_menu()
    user = int(input("Pick an Option: "))
    if user == 1:
        add_task()
    elif user == 2:
        view_tasks()
    elif user == 3:
        complete_task()
    elif user == 4:
        edit_task()
    elif user == 5:
        delete_task()
    elif user == 6:
        filter_tasks()
    elif user == 7:
        print("Okay, Have a nice day")
    else:
        print("Invalid Input")
