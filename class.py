print(type(1))
print(type('D'))
print(type(True))


class car:
    speed = 0
    started = False

    def start(self): # This is a method
        self.started = True
        print("Car started, Okay Let's go on a ride!!")

    def increase_speed(self, delta):
        if self.started:
            self.speed = self.speed + delta
            print("Vroooooom")
        else: 
            print("You need to start the car first!")

    def stop(self):
        self.speed = 0
        print("Halting")


car1 = car()
car1.start()
car1.increase_speed(20)
car1.stop()


# class BankAccount:
#     # balance = 0
#     # account_holder = "Damilola" it's not needed cos of init

#     def __init__(self, account_holder, balance):
#         self.account_holder = account_holder
#         self.balance = balance
    
#     def deposit(self, amount):
#         self.balance = self.balance + amount
#         print("Okay, Deposit Successful!")

#     def withdraw(self, amount):
#         if self.balance >= amount:
#             self.balance = self.balance - amount
#             print(f"{amount} has been withdrawn")
#         else:
#             print("Insufficient Funds")

#     def check_balance(self):
#         if self.balance <= 0:
#             print("Your account is empty like your head")
#         else:
#             print(f"Your balance: {self.balance}")


# account1 = BankAccount("Damilola", 15000)
# account2 = BankAccount("Jair", 25000)
# account3 = BankAccount("Mary", 5000)
# account1.deposit(10000)
# account1.withdraw(3000)
# account1.check_balance()
# account1.withdraw(9000)
# account1.check_balance()


class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"

    def introduce(self):
        print(f"My name is {self.name} and I am {self.age} years old.")

    def celebrate_birthday(self):
        # self.age = age
        self.age = self.age + 1
        

person1 = person("Damilola", 25)
person2 = person("Long Jun", 30)
person1.introduce()
print(person1)
person1.celebrate_birthday()
person1.celebrate_birthday()
print(person1.age)
print(person2)
message = person2.introduce()
print(message)


class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount
        print(f"{amount} has been deposited")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance = self.balance - amount
            print(f"{amount} has been withdrawn")
        else:
            print("Insufficient Funds")

    def transfer(self, amount, recipient):
        if self.balance >= amount:
            self.balance = self.balance - amount
            recipient.balance = recipient.balance + amount
            print(f"{amount} Successfully transfered to {recipient.account_holder}")
        else:
            print("Insufficient Funds")

    def check_balance(self):
        if self.balance <= 0:
            print("Lol, What are you looking for? Don't tell me you didn't know your account was empty")
        else:
            print(f"Your balance: {self.balance}")


account1 = BankAccount("Damilola", 50000)
account1.deposit(10000)
account1.check_balance()
account1.withdraw(20000)
account1.check_balance()
account2 = BankAccount("Samuel", 20000)
account1.transfer(10000, account2)
account1.check_balance()
account2.check_balance()

