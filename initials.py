def get_initials():
    name = input("What is your full name?")
    upper_name = name.upper()

    for i in (upper_name):
        if i == " ":
            print(upper_name[ord(i) + 1])

get_initials()
