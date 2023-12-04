import string
import random

characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")

def generate_password():
    password_length = int(input("Please input your desired password length: "))
    
    if password_length < 8:
        print("Please password length can not be less than 8 characters")
        quit()
    else:
        random.shuffle(characters)

    password = []

    for x in range(password_length):
        password.append(random.choice(characters))

    random.shuffle(password)

    password = "".join(password)
    print(password)

option = input("Do you want an auto generated password? (Yes/No): ")
if option.lower() == "yes":
    generate_password()
elif option.lower() == "no":
    print("exiting....")
    quit()
else:
    print("Invalid input, you can only enter Yes/No thanks.")