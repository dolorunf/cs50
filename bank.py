text = input("Ask for greeting: ")
if text.lower().strip().startswith("hello"):
    print("$0")
elif text.lower().strip().startswith("h"):
    print("$20")
else:
    print("$100")