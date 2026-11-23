# # """
# # x = 9
# # print(f'The price is {x:.2f} dollars')
# # """

# # age = 36
# # txt = f"My name is John, I am {age}"
# # print(txt)

# # txt = "We are the so-called \"Vikings\" from the north."
# # print(txt)

# # txt = "Hello World"
# # print(txt[0])

# # txt = "Hello World"
# # print(txt[2:5])

# # print(10 > 9)
# # print(10 == 9)
# # print(10 < 9)

# # a = 400
# # b = 70
# # if b > a:
# #     print("b is greater than a")
# # else:
# #     print("b is not greater than a")

# # x = "Hello"
# # y = 15

# # print(bool(x))
# # print(bool(y))

# # print(bool("abc"))
# # print(bool(123))
# # print(bool(["apple", "cherry", "banana"]))

# # print(bool(False))
# # print(bool(None))
# # print(bool(0))
# # print(bool(""))
# # print(bool(()))
# # print(bool([]))
# # print(bool({}))

# # def myFunction() :
# #   return True

# # if myFunction():
# #   print("YES!")
# # else:
# #   print("NO!") 

# # print(10 + 5)

# # sum1 = 150 + 56
# # sum2 = sum1 - 100
# # sum3 = sum2 * 200
# # print(sum1)
# # print(sum2)
# # print(sum3)

# # x = 25
# # y = 10

# # print(x + y)
# # print(x - y)
# # print(x * y)
# # print(x / y)
# # print(x % y)
# # print(x ** y)
# # print(x // y)

# # x = 8
# # x |= 3
# # print(x)

# # numbers = [1, 2, 3, 4, 5]

# # if (count := len(numbers)) > 3:
# #     print(f"List has {count} elements")

# # num = 6
# # x = "WEEKEND!"  if num > 5 else "Workday"

# # print(x)

# # num = 6

# # x = "Fri" if num == 5 else "Sat" if num == 6 else "Sun" if num == 7 else "weekday"

# # print(x)

# # x = 7
# # y = 10

# # print(x == y)
# # print(x != y)
# # print(x < y)
# # print(x > y)
# # print(x <= y)
# # print(x >= y)
# # print(1 < x < 10)


# # text = "Hello World"
# # print("H" in text)
# # print("hello" in text)
# # print("z" not in text)

# # print((6 + 3) - (6 + 3))
# # print(100 + 5 ** 3)

# # # Create variables
# # a = 15
# # b = 4
# # # Print modulus
# # print(a % b)
# # # Print floor division
# # print(a // b)
# # # Print power
# # print(a ** b)
# # # Add 10 to a
# # a += 10

# # mylist = ["apple", "cherry", "banana"]
# # print(mylist)

# # mylist = ["apple", "cherry", "banana", "orange", "apple", "banana", "pineapple"]
# # print(len(mylist))

# # list1 = ["apple", "cherry", "banana"]
# # list2 = [1, 2, 3, 4, 5]
# # list3 = [True, False, True]
# # print(list1[0])
# # print(list2[4])
# # print(list3[-1])

# # mylist = ["apple", "banana", "cherry"]
# # print(type(mylist))

# # age = 22
# # print(type(age))

# # carname = "Brabus"
# # print(type(carname))

# # thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# # print(thislist[2:5])

# # thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# # print(thislist[-2:-5:-1])
# # print(thislist[-5:-2])
# # if "kiwi" in thislist:

# #   print("Yes, 'kiwi' is in the list")

# # mylist = ["kiwi", "apple", "cherry", "orange"]
# # mylist[0] = "pineapple"
# # print(mylist)

# # thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
# # thislist[1:3] = ["blackcurrant", "watermelon"]
# # print(thislist)

# # thislist = ["apple", "banana", "cherry"]
# # thislist[1:3] = ["watermelon"]
# # print(thislist) 

# # mylist = ["watermelon", "kiwi", "banana", "mango"]
# # mylist.insert(3, "dates")
# # mylist.append("apple")
# # print(mylist)

# # mylist = ["orange", "kiwi"]
# # tropical = ["mango", "pineapple"]
# # mylist.extend(tropical)
# # mylist.remove("mango")
# # mylist.pop()
# # del mylist[0]
# # print(mylist)


# # num2 = [1, 2, 3, 4]
# # num3 = [5, 6, 7, 9]
# # num2.extend(num3)
# # print(num2)

# # thislist = ["apple", "banana", "cherry"]
# # for x in thislist:
# #   print(x)

# # mylist = ["watermelon", "pineapple", "orange", "kiwi"] # to loop through a list
# # for y in mylist:
# #    print(y)

# # for i in range(len(mylist)): # loop through the index numbers
# #    print(mylist[i])

# # mylist = ["watermelon", "pineapple", "orange", "kiwi"] # using list comprehension
# # [print(y) for y in mylist]


# # thislist = ["apple", "banana", "cherry"] # using a while loop
# # i = 0
# # while i < len(thislist):
# #   print(thislist[i])
# #   i = i + 1

# # fruits = ["watermelon", "pineapple", "orange", "kiwi", "mango"]
# # newlist = []

# # for x in fruits:
# #    if "a" in x:
# #       newlist.append(x)
# # print(newlist)     

# # fruits = ["watermelon", "pineapple", "orange", "kiwi", "mango"] # doing all in one line of code
# # newlist = [x for x in fruits if "a" in x]
# # print(newlist)

# # '''
# # # guess the number project

# # secret = 8
# # guess = int(input("Guess the number: "))

# # if secret == guess:
# #    print("You got it")
# # else:
# #    print("Wrong answer")

# # '''

# # fruits = ["watermelon", "pineapple", "orange", "kiwi", "mango"] # to capitalize
# # newlist = [x.upper() for x in fruits]
# # print(newlist)


# # fruits = ["watermelon", "pineapple", "orange", "kiwi", "mango"] # to replace one fruit with the other
# # newlist = [x if x != "watermelon" else "apple" for x in fruits]
# # print(newlist)

# # # to sort ascending
# # thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
# # thislist.sort()
# # print(thislist)

# # thislist = [7, 0, 3, 5, 2, 8, 9] 
# # thislist.sort()
# # print(thislist)

# # # to sort descending
# # fruits = ["watermelon", "pineapple", "orange", "kiwi", "mango"]
# # fruits.sort(reverse= True)
# # print(fruits)

# # def myfunc(n):
# #   return abs(n - 50)

# # thislist = [100, 50, 65, 82, 23]
# # thislist.sort(key = myfunc)
# # print(thislist)

# # thislist = ["banana", "Orange", "Kiwi", "cherry"]
# # thislist.sort()
# # print(thislist)

# # thislist = ["banana", "Orange", "Kiwi", "cherry"]
# # thislist.reverse()
# # print(thislist)


# # thislist = ["banana", "Orange", "Kiwi", "cherry"] # to make a copy f list
# # mylist = thislist.copy()
# # print(mylist)


# # thislist = ["banana", "Orange", "Kiwi", "cherry"] # using slice operator to make a copy
# # mylist = thislist[:]
# # print(mylist)

# # # tuplesllow duplicate,it is indexed, ordered nd unchangeable. written with round bracket()
# # mytuple = ("apple", "banana", "pawpaw", "apple")  # this is called packing a tuple
# # thistuple = ("pineapple",)
# # print(mytuple)
# # print(len(mytuple))
# # print(thistuple)
# # print(mytuple[0])
# # print(mytuple[-1])

# # tuple1 = ("Dami is", 22, "years old", True)
# # print(tuple1)
# # print(type(tuple1))

# # tuple1 = ("Dami is", 22, "years old", True)# IN to check a specific item in python
# # if "it" in tuple1:
# #    print("yes, 22 is in tuple1")
# # else:
# #    print("Not found in tuple1")
# # print(len(tuple1))

# # a = ("pineapple", "mango", "pawpaw")
# # b = list(a) # i used list to update my tuple since tuple is unchangeable
# # a = tuple(b)
# # b[0] = "orange"
# # b.append("kiwi") # to add an item to a tuple
# # print(a)
# # print(b)
# # # or add tuples to tuples 

# # a = ("orange", "mango", "kiwi", "pineapple", "banana") # to add a tuple to a tuple create a new tuple and us += to add to the first tuple **note to create a new tuple add a (,) after the item
# # b = ("pawpaw",)
# # a += b
# # b = list(a) # convert a which is tuple into list which is b
# # b.remove("kiwi") # to remove an item after turning a to a list
# # print(a)
# # print(b)
# # '''
# # thistuple = ("orange", "mango", "kiwi", "pineapple", "banana")
# # del thistuple
# # print(thistuple)
# # '''

# # name = ("Darina", "Kedar", "Kemuel")
# # (Journalist, CEO, Basketballplayer) = name
# # print(Journalist)
# # print(CEO)
# # print(Basketballplayer)

# # thistuple = ("orange", "mango", "kiwi", "pineapple", "banana")
# # (yam, maize, *rice) = thistuple  # * to collect the remaining values as a list
# # print(yam)
# # print(maize)
# # print(rice)

# # thistuple = ("orange", "mango", "kiwi", "pineapple", "banana")
# # for j in range(len(thistuple)):
# #     print(thistuple[j])

# # thistuple = ("orange", "mango", "kiwi", "pineapple", "banana")
# # j = 0
# # while j < len(thistuple):
# #     print(thistuple[j])
# #     j = j + 1

# # names = ("Dami", "Prince", "John")
# # actions = ("Sleeps", "Codes", "Eats")
# # for name in names:
# #     for action in actions:
# #         print(name + " " + action + ".")


# # # name = input("Enter your name: ")
# # # while name == "":
# # #     print("You did not enter your name")
# # # else:
# # #     print("Hello " + name)


# # # age = int(input("Enter your age: "))

# # # if age <= 0:
# # #     print("Age can't be negative or zero")
# # # else:
# # #     print(age)

# # for x in reversed(range(2, 11, 2)):
# #     print(x)

# # print("MERRY CHIRSTMAS!")

# # for x in range(1, 21):
# #     if x == 11:
# #         break
# #     else:
# #         print(x)  

# # for i in range(1, 51, 2):
# #     if x == 25:
# #         continue
# #     else:
# #         print(i)


# # # Exercises on [for loop in python]
# # # 1. use whie loop to print first natural numbers
# # i = 1
# # while i <= 10:
# #     print(i)
# #     i += 1

# # # 2, use a for loop to display numbers from -10 to -1

# # for x in range(-10, 0):
# #     print(x)

# # # 3 write a program that display "Done" after successful execution of for loop
# # for j in range(0, 5):
# #     print(j)
# # print("Done!")    

# # # #4 calculate the sum of all numbers from 1 to n
# # # n = int(input("Enter number: "))
# # # s = 0
# # # for i in range(1, n + 1): # we atrt counting from 1 nd ends at the n
# # #    s += i
# # # print("Sum is:", s)

# # # #5 to calculate the multiplication of a given number
# # # n = 2
# # # for y in range(1, 11):
# # #     print(n * y)

# # # #6 to calculate the cube of numbers from 1 to 6
# # # n = int(input("Enter input_number: "))
# # # s = 0
# # # input_number = 6

# # # for y in range(1, input_number + 1):  
# # #     print(f"Current Number is : {y} and the cube is {y ** 3}") # f tells python to look into the {} and replace the variables with their actual values

# # # 7 Display number from a list using a loop
# # numbers = [12, 75, 150, 180, 145, 525, 50]
# # for item in numbers:
# #      if item > 500:
# #          break
# #      elif item > 150:
# #          continue
# #      elif item % 5 == 0:
# #         print(item)

# # # 8 count occurrences of a specific element 
# # list1 = [10, 20, 10, 30, 10, 40, 50]
# # target = 10
# # count = 0
# # for item in list1:
# #    if item == target:
# #       count += 1

# # print(f"{target} appears {count} times")

# # # 9 print eements frm a list present at odd index position
# # my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# # for x in range(1, len(my_list), 2):

# #    print(my_list[x])

# # # to reverse using loop
# # list1 = [10, 20, 30, 40, 50]
# # for i in reversed(list1):
# #    print(i)

# # Original = "Python"
# # reversed_str = ""
# # for char in Original:
# #    reversed_str = char + reversed_str

# # print(f"Original: {Original}")
# # print(f"Reversed: {reversed_str}")




# # i = 1
# # while i <= 10:
# #    print(i)
# #    i += 1

# # for i in range(-10, 0):
# #    print(i)

# # for x in range(0, 5):
# #    print(x)
# # print("Done!")

# # n = int(input("Enter number: "))
# # s = 0
# # for x in range(1, n + 1):
# #    s += x
# # print("Sum is:",s)


# # n = 2
# # for i in range(1, 11):
# #    print(i * 2)

# # input_number = 6
# # for i in range(1, input_number + 1):
# #    print(f"Current Number is: {i} and the cube is {i ** 3}")


# # numbers = [12, 75, 150, 180, 145, 525, 50] 
# # for item in numbers:
# #     if item > 500:
# #        break
# #     elif item > 150:
# #        continue
# #     elif item % 5 == 0:
# #         print(item)


# # list1 = [10, 20, 10, 30, 10, 40, 50]
# # target = 10
# # count = 0
# # for item in list1:
# #     if item == target:
# #         count += 1
# # print(f"{target} appears {count} times")   


# # my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# # for x in range(1, len(my_list), 2):
# #     print(my_list[x], end= " ")

# # list1 = [10, 20, 30, 40, 50]
# # for c in reversed(list1):
# #     print(c)

# # Original: "Python"
# # reversed_str = ""
# # for char in Original:
# #     reversed_str = char + reversed_str
# # print(f"Original: {Original}")
# # print(f"Reversed: {reversed_str}")


# # # sentence = "Loops are Fun!"
# # # vowels = "aeiou"
# # # vowels_count = 0
# # # consonants_count = 0

# # # for char in sentence:
# # #     if char.isalpha():
# # #         if char.lower() in vowels:         
# # #              vowels_count += 1
# # #             elif:       
# # #              consonants_count += 1
# # # print(f"Vowels: {vowels_count}")
# # # print(f"Consonants: {consonants_count}")

# # # sentence = "Loops are Fun"
# # # vowels = "aeiou"
# # # count_vowels = 0
# # # count_consonants = 0

# # # for char in sentence.lower():
# # #    if char.isalpha():
# # #       if char in vowels:
# # #           count_vowels += 1
# # #    else:
# # #       count_consonants += 1

# # # print(f"Vowels: {count_vowels}")
# # # print(f"Consonants: {count_consonants}")

# # thistuple = ("apple", "banana", "cherry")
# # i = 0
# # while i < len(thistuple):
# #     print(thistuple[i])
# #     i = i + 1 

# # dami = (1, 2, 4, 6)
# # j = 0
# # while j < len(dami):
# #     print(dami[j])
# #     j += 1

# # tuple1 = ("a", "b", "c")
# # tuple2 = (1, 2, 3)
# # tuple3 = tuple1 + tuple2
# # print(tuple3)

# # fruits = ("pineapple", "mango", "orange")
# # fruit = fruits * 4
# # print(fruit)


# # fruits = ("apple", "banana", "cherry")
# # print(fruits[1]) # to print the second item
# # print(len(fruits)) # to check for the length of fruits
# # (a, b, c) = fruits # to unpack the tuple
# # print(b)

# # list = set(("apple", "banana", "kiwi", "apple", True, 1, 5, False, 0, 5, 7))                                                                           
# # print(type(list))
# # print(len(list))
# # print(list)

# # myset = {1, 2, 4, 5, 6, 7}
# # myset.add("Dami")
# # for i in myset:
# #     print(myset) # to print the whole set for every item
# #     #print(i) # to print the curent item
# #     #print(5 in myset) # check if 5 is present in myset if true it prints
# #     #print(1 not in myset) # check if 1 is not in present if its present     

# myset = {1, 3, 6, 7, 8, 9}
# list = ["pineapple", "banana", "apple"]
# myset.update(list)  # to add anoter set,list,tupleor dictionaries to the current set use update() method
# myset.remove(3)  # to remove item from the set
# myset.discard("pineapple")  # to remove pineapple 
# i = myset.pop()  # to remove a random item
# print(myset)
# print(i)  # to print the item pop removed


# set = {"apple", "banana", "cherry"}
# set.clear()
# print(set)

# # thisset = {"apple", "banana", "cherry"}
# # del thisset
# # print(thisset)

# fruit = {"pineapple", "pawpaw", "date"}
# for x in fruit:
#     print(x)

# set1 = {"a", "b", "c"}
# set2 = {1, 2, 3}
# set3 = set2.union(set1)  # to rturn set3 as the combination of both set1nd 2
# print(set3)

# set1 = {"a", "b", "c"}
# set2 = {1, 2, 3}
# set3 = set1 | set2  # using the | operator to get the same result as union
# print(set3)

# set1 = {"a", "b", "c"}
# set2 = {1, 2, 3}
# set3 = {"Mimi", "Reyna"}
# set4 = {"cherry", "banana", "orange"}
# set = set1.union(set2, set3, set4)  # to join multiple sets
# print(set)

# set1 = {"a", "b", "c"}
# set2 = {1, 2, 3}
# set3 = {"Mimi", "Reyna"}
# set4 = {"cherry", "banana", "orange"}
# set = set1 | set2 | set3 | set4  # to join multiple sets
# print(set)

# x = {"a", "b", "c"}
# y = (1, 2, 3)
# z = x.union(y)  # allow joinig sets with other data type like tuples, list
# print(z)

# x = {"a", "b", "c"}
# y = {1, 2, 3, "b"}
# z = x.intersection(y)  # to return a new set that is present in both existing sets, accept other data types
# print(z)

# x = {"apple", "banana", "cherry"}
# y = {"google", "microsoft", "apple"}


# z = x & y  # to return a new set as well as the intersection
# x.intersection_update(y)  # change the original set instead of returning a new set
# print(x)
# print(z)

# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}
# set3 = set1.difference(set2)  # will only return a new set that is in set1 but not in set2
# print(set3)

# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}
# set3 = set1 - set2    # same as differences works, for only sets
# print(set3)

# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}
# set1.difference_update(set2)  # change the original set instead of returning a new set
# print(set1)

# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}
# set3 = set1.symmetric_difference(set2)  # return items that are NOT PRESENT in both sets
# print(set3)

# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}
# set3 = set1 ^ set2  # same as symmetric_difference work but only for sets unlike symmetric_difference
# print(set3)

# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}
# set1.symmetric_difference_update(set2)  # change the original set instead of returning a new set
# print(set1)


# x = frozenset(["apple", "banana", "cherry"])
# print(x)
# print(type(x))

# # for j in range(1, 6):
# #     print(j)

# # x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# # for i in range(len(x)):
# #     print(x[i], end=" ")

# # print()

# # for i in range(97, 123):
# #     print(chr(i), end=" ")

# # print()

# # for j in range(65, 91):
# #     print(chr(j), end=" ")

# # print()  

# # x = [1, 2, 3, 4, 5]
# # for i in range(len(x)):
# #     print(x[i])

# # for i in range(1, 50):
# #     if i == 31:
# #         continue
# #     print(i)


# for i in range(1, 6):
#     print(i)


# j = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# for i in range(len(j)):
#     print(j[i], end=" ")

# print()

# for i in range(65, 91):
#     print(chr(i), end=" ")

# print()

# for i in range(0, 100, 5):
#     if i == 45:
#         continue
#     if i == 50:
#         break
#     print(i, end=" ")

# print()

# for i in reversed(range(0, 6)):
#     print(i)
# print("HAPPY NEW YEAR!")

# # secret = 7
# # Guess = int(input("Guess the number: "))
# # if Guess == secret:
# #     print("You are right!")
# # else:
# #     print("Wrong Answer")


# def israining():
#     text = input("is it raining? ").lower()
#     if text == "yes":
#         print("You need an umbrella")
#     else:
#         print("What a beautiful weather!")


# israining()

# value = "python"
# for i in reversed(value):
#     print(i, end="")

# print()


# milk_ounces = 16
# pour_amount = 6

# remaining = milk_ounces - pour_amount

# print(remaining)

# cereal_in_box = 10
# required_scoops = 3
# if cereal_in_box <= required_scoops:
#     print(True)
# else:
#     print(False)

# value1 = "15"
# value2 = "banana"
# print(value1.isdigit())
# print(value2.isdigit())


# selected_drink = "Green Tea"
# target_temp = 100
# if selected_drink == "Green Tea":
#     target_temp = 80
# elif selected_drink == "Tea":
#     target_temp = 90
# print(target_temp)

# for count in range(5):
#     print("count " + str(count)) 

# weight = 0.0
# while weight < 1.5:
#     weight = weight + 0.5
#     print("Current weight: " + str(weight))


# def eligibility_logic(score, attendance, completed_drill):

#     if score >= 70 and attendance >= 80 and completed_drill is True:       
#         return ("Eligible")
#     else:
#         return ("Not eligible")


# score = 80
# attendance = 90
# completed_drill = False

# print(eligibility_logic(score, attendance, completed_drill))


# def safe_calculator(a, operator, b):
#     if operator == "+":
#         return (a + b)
#     elif operator == "-":
#         return (a - b)
#     elif operator == "*":
#         return (a * b)
#     elif (operator == "/" or operator == "%") and b == 0:
#         return ("Cannot divide by zero")
#     elif operator == "/":
#         return round(a / b, 2)
#     elif operator == "%":Increase memory for more
#         return (a % b)
#     elif operator == "**":
#         return (a ** b)
#     else:
#         return ("Invalid operator")
    
    
# a = 5
# operator = "+"
# b = 3

# print(safe_calculator(a, operator, b))


# order = " espresso "
# print(order.strip().capitalize())   # Capitalize the first lwtter


# name = "Ninioluwalere"
# print(name[:9])

# customer = "Reyna"
# total = 12.0
# print(f"Order for {customer}\nTotal: ${total}")


# sentence = "latte and espresso"
# print(sentence.replace(" and ", "-"))


# def greet():
#     name = input("What's your name? ")
#     print('Good Afternoon', name)


# greet()


# def order_drink(drink, size):
#     print("Dispensing " + size + " " + drink)


# order_drink("espresso", "large")

# # order_drink()

# name = input("What is your name? ").strip().capitalize()
# print(f" Hello, {name}")   # to captalize title


# def mix_ingredients(liquid, powder):
#     print("Mixing " + liquid + " with " + powder)


# mix_ingredients("milk", "cocoa")


# def get_guess():
#     guess = get_guess
#     if guess == 45:
#         print("WOW, you got it right!")
#     else:
#         print("Oops, try again")


# def main():
#     guess = int(input("Enter a guess: "))
#     return guess


# main()


# thisdict = {
#     "Brand": "Mercedes-Benz",
#     "Model": "G-Wagons",
#     "Tuner": "Brabus",
#     "Year": 2025
# }
# print(len(thisdict))


def test_scope():
    secret_recipe = "Vanilla Syrup"
    return secret_recipe


secret_recipe = test_scope()

print(secret_recipe)


total_sales = 0.0


def record_sale(amount):
    global total_sales
    total_sales = total_sales + amount
    print(f"Sale recorded: ₦{amount:.2f}")


record_sale(4.50)


count = 0


def increment():
    global count
    count = count + 1
    print(count)


increment()
increment()
increment()
increment()


global_sales = 0


def make_drink():
    global local_count
    local_count = 0  # Born fresh on every function call

    local_count = local_count + 1
    global global_sales
    global_sales = global_sales + 1
    print(f"Local: {local_count}, Global: {global_sales}")

    
make_drink()
make_drink()
make_drink()
make_drink()


function greet() {
    console.log("Hello!");
}

greet();