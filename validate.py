import re

# email = input("Enter your email address: ").strip()
# # if '@' and '.' in email:
# #     print("Valid")
# # else:
# #     print("Invalid")
# if re.search(r'^.+@.+\.com$', email):
#     print('valid')
# else:
#     print('Invalid email')


# import re

email = input("Enter your email address: ")
if re.search(r"^.+@.+\.com$", email):
    print("Valid email")
else:
    print("Invalid email")
