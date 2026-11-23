def main():
    names = ("Aang", "Zuko", "Appa", "Katara", "Sokka", "Momo", "Uncle Iroh",
             "Toph")
    for name in range(len(names)):
        print(write_letter(names[name]))


def write_letter(receiver):
    return f"""
---------------------------------------------
        Dear {receiver},
        You are invited to my birthday this Saturday.
        Hope you can make it!
        Angela
----------------------------------------------
    """


main()