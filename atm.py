account_balance = 0
secret_code = 250304
atm_pin = 2004


def show_menu():
    print("WELCOME TO FTD BANK!!!")
    print("What service would you like us to provide? ")
    print("1. Check my balance")
    print("2. Deposit money")
    print("3. Withdraw money")
    print("4. Transfer money to others")
    print("5. Exit")


def check_balance(account_balance):
    print("Your Account Balance:", account_balance)


def deposit_money(account_balance):
    dep = int(input("How much do you want to deposit? "))
    if dep <= 0:
        print("Enter a valid amount")
    else:
        account_balance += dep
        print(f"You have successfully deposited {dep}")
    return account_balance


def withdraw_money(account_balance):
    wit = int(input("How much do you want to withdraw? "))
    if wit <= 0:
        print("Enter a valid amount")
    elif wit > account_balance:
        print("Insufficient Balance")
    else:
        account_balance -= wit  
        print(f"{wit} has been successfully withdrawn!")
    return account_balance


def transfer_money(account_balance):
    trans = input("Enter the valid account number? ")
    if len(trans) == 10 and trans.isdigit():
        print("Valid account number")
    else:
        print("Enter a valid account number")
        return account_balance
    amount = int(input("Enter amount to transfer: "))
    if amount >= account_balance:
        print("Insufficient Balance")
    else:
        ask = int(input("input your 4 digits pin: "))
        if ask == atm_pin:
            account_balance -= amount
            print(f"{amount} has been sent")
            
        else:
            print("Enter correct pin: ")
            ask = int(input("input your 4 digits pin: "))
            if ask == atm_pin:
                account_balance -= amount
                print(f"{amount} has been sent")
            else:
                print("Enter correct pin please")
    return account_balance


enter = int(input("Enter your secret code: "))
if enter == secret_code:
    user = 0
    while user != 5:
        show_menu()    

        user = int(input("Pick an option: "))
        if user == 1:
            check_balance(account_balance)
        elif user == 2:
            account_balance = deposit_money(account_balance)
        elif user == 3:
            account_balance = withdraw_money(account_balance)
        elif user == 4:
            account_balance = transfer_money(account_balance)
        elif user == 5:
            print("Have a nice day!")
        else:
            print("Oops option doesn't exist here")
else:
    print("Invalid code!")

