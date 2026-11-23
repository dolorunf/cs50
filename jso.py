# # import json

# # # json.dumps() to convert python data to a json string
# # # json.loads() to convert json string to a python data
# # # json.dump() write python data to a file
# # # json.load() read json data to a file
# # student = {
# #     "name": "Avianna",
# #     "age": 2,
# #     "is_learning": True
# # }

# # result = json.dumps(student)
# # print(result)

# # # import json

# # student = {
# #     "name": "Dammy",
# #     "age": 20,
# #     "is_learning_python": True
# # }
# # with open("question.json", "w") as file:
# #     json.dump(student, file)

# # # import json

# # try:
# #     with open("tasks.json", "r") as file:
# #         tasks = json.load(file)
# # except FileNotFoundError:
# #     tasks = []

# # print(tasks)


# # # Pillow used to manipulated iamages within python
# # # from PIL import Image
# # # from PIL import ImageFilter to acces filters
# # # def main():
# # #     with image.open("in.jpeg") as image:
# # #         img = img.rotates(180) to rotate the image
# # #         img.filter(ImageFilter.BLUR)
# # #         img.save("out.jpeg")
# # # main()

# # # to create a class
# # class MyClass:
# #     x = 6


# # print(MyClass)

# # # Objects
# # p1 = MyClass()
# # print(p1.x)


# # class Student:
# #     def _init_(self, name, age):
# #         self.name = name
# #         self.age


# # class Person:
# #     def __init__(self, name, age):
# #         self.name = name
# #         self.age = age

# #     def greet(self):
# #         print("Hello, my name is " + self.name)


# # p1 = Person("John", 36)
# # p1.greet()


# # if total == 0:
# #     return 0
# # return round((len / width)*100)


# # for index, balance in enumerate(balances):
# #     if balance < index:
# #         returnindex
# # return -1

# # lis = list(map(lambda x: x.strip().lower(), normalize))
# # return lis

# # spending = {}
# # for i in expenses:
# #     if i['category'] in spending:
# #         spending[i['category']] += i['amount']
# #     else:
# #         spending[i['category']] = i['amount']

# # for item in spending.items:
# #     return spending

# # lis = list(map(lambda x: x.strip().lower(), normalize))
# # return lis

# # for index, balance in enumerate(balances):
# #     if balance < index:
# #         return index
# # return -1

# # def count_correct(questions, answers):
#     score = 0
#     for question, answer in zip(questions, answers):
#         if answer == question['answer']:
#             score += 1
#     return score

#     score = 0
#     for question, answer in zip(questions, answers):
#         if answer == question['answer']:
#             score += 1
#     return score
#     score = 0
#     for question, answer in zip(questions, answers):
#         if answer == question['anser']
#         score += 1

#         for task in tasks:
#             if task.get("id") == tasks:
#                 return task
#         return None
    
import re

text = "Hello, My name is Damilola"
result = re.findall(r"\w", text)
print(result)