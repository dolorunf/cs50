def main():
    # print(write_letter("Jeo", "Joy"))
    # print(write_letter("Tiny", "Joy"))
    names = ("Jeo", "Tiny", "Reyna", "Quiana")
    for i in range(len(names)):
        print(write_letter(names[i], "Joy"))


def write_letter(receiver, sender):
    return f"""
    ------------------------------------------
        Dear {receiver},

        You are cordially invited to a ball at 
        Joy's Castle this evening, 7:00 PM.

        Sincerely,
        {sender}
    --------------------------------------------
    """


main()