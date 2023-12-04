def add(a, b):
    solution = a + b
    answer = print(str(a) + "+" + str(b) + " = " + str(solution))
    return answer

def sub(a, b):
    solution = a - b
    answer = print(str(a) + "-" + str(b) + " = " + str(solution))
    return answer

def mul(a, b):
    solution = a * b
    answer = print(str(a) + " * " + str(b) + " = " + str(solution))
    return answer

def div(a, b):
    solution = a / b
    answer = print(str(a) + " / " + str(b) + " = " + str(solution))
    return answer

while True:
    print("A. Addition")
    print("B. Subtraction")
    print("C. Multiplication")
    print("D. Division")
    print("E. Exit")

    choice = input("Please select a choice for your calculation: ")

    if choice == "a" or choice == "A":
        print("Addition")
        a = int(input("Please enter your first number: "))
        b = int(input("Please enter your second number:"))
        add(a, b)
    elif choice == "b" or choice == "B":
        print("Subtraction")
        a = int(input("Please enter your first number: "))
        b = int(input("Please enter your second number:"))
        sub(a, b)
    elif choice == "c" or choice =="C":
        print("Multiplication")
        a = int(input("Please enter your first number: "))
        b = int(input("Please enter your second number:"))
        mul(a, b)
    elif choice == "d" or choice == "D":
        print("Division")
        a = int(input("Please enter your first number: "))
        b = int(input("Please enter your second number:"))
        div(a, b)
    elif choice == "e" or choice == "E":
        print("Exiting...")
        quit()