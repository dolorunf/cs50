# # def calculate_love_score(name1, name2):
# #     names = (name1 + name2).lower()
# #     nameT = names.count("t")
# #     nameR = names.count("r")
# #     nameU = names.count("u")
# #     nameE = names.count("e")
# #     total = nameT + nameR + nameU + nameE
# #     # print(total)
# #     nameL = names.count("l")
# #     nameO = names.count("o")
# #     nameV = names.count("v")
# #     nameE = names.count("e")
# #     love_score = nameL + nameO + nameV + nameE
# #     print(str(total) + str(love_score))


# # calculate_love_score("hop e", "Tominion")


# def calculate_love_score():
#     name1 = input("What's name1? ")
#     name2 = input("What's name2? ")
#     names = (name1 + name2).lower()
#     true_count = 0
#     love_count = 0

#     for letter in names:
#         if letter in "true":
#             true_count += 1
#     for letter in names:
#         if letter in "love":
#             love_count += 1
#     print(str(true_count) + str(love_count))


# calculate_love_score()    


# def calculate_adventure_score(name1, name2):
#     names = (name1 + name2).lower()
#     brave_count = 0
#     wild_count = 0
#     for letter in names:
#         if letter in "brave":
#             brave_count += 1
#     for letter in names:
#         if letter in "wild":
#             wild_count += 1
#     print(str(brave_count) + str(wild_count))


# calculate_adventure_score("David", "Brenda")


# account_balance = 50000
# user = 0 
# password = 2004
# while user != 4:  
#     ask = int(input("Enter your 4 digits Pin: ")) 
#     if ask == password:
        
#         print("WELCOME TO THE ATM MACHINE STAND")
#         print("1. Check balance")
#         print("2. Deposit money")
#         print("3. Withdraw money")
#         print("4. Exit")
#         user = int(input("Pick an option: "))
#         if user == 1:
#             print("Your Account Balance:", account_balance)
#         elif user == 2:
#             deposit = int(input("How much do you want to deposit? "))
#             account_balance += deposit
#             print(f"You have successfully deposit {deposit}")

#         elif user == 3:
#             withdraw = int(input("How much do you want to withdraw? "))
#             if withdraw > account_balance:
#                 print("Insufficient Balance")
#             else:
#                 account_balance -= withdraw
#                 print(f"{withdraw} successfully ")
#         elif user == 4:
#             print("Have a nice day!")       
#         else:
#             print("Oops option doesn't exist here")
#     else:
#         print("Incorrect Pin!")
    

account_balance = 50000
password = 2004

ask = int(input("Enter your 4 digits Pin: "))

if ask == password:

    user = 0

    while user != 5:

        print("WELCOME TO THE ATM MACHINE STAND")
        print("1. Check balance")
        print("2. Deposit money")
        print("3. Withdraw money")
        print("4. Transfer money to others")
        print("5. Exit")

        user = int(input("Pick an option: "))

        if user == 1:
            print("Your Account Balance:", account_balance)

        elif user == 2:
            deposit = int(input("How much do you want to deposit? "))
            account_balance += deposit
            print(f"You have successfully deposited {deposit}")

        elif user == 3:
            withdraw = int(input("How much do you want to withdraw? "))
            ask_user = input("Enter your password: ")
            if ask_user == password:
                if withdraw >= account_balance:                                                              
                    print("Insufficient Balance")               
                else:
                    account_balance -= withdraw
                    print(f"{withdraw} successfully withdrawn")
            else:
                print("Password not correct")
        elif user == 4:
            account_number = input("Enter Recipent 10 digits Account Number: ")
            if len(account_number) == 10 and account_number.isdigit():
                print("Valid account number")
            else:
                print("Enter the correct account number: ")
            amount = int(input("Enter Amount to send: "))
            # account_balance -= amount
            if amount >= account_balance:
                print("Insufficient Balance")
            else:

                enter = int(input("Enter your 4 digits Pin: "))
                if enter == password:
                    account_balance -= amount
                    print(f"{amount} Transferred Successfully")
                else:
                    print("Enter correct password")
                
        elif user == 5:
            print("Have a nice day!")

        else:
            print("Oops option doesn't exist here")

else:
    print("Incorrect Pin!")