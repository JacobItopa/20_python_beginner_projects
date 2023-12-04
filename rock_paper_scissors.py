import random

user_score = 0
computer_score = 0

exit = False

while exit == False:
    options = ["rock", "paper", "scissors"]
    user_option = input("Please select an option from (Rock, Paper, Scissors or Exit): ")
    computer_option = random.choice(options)

    if user_option == "exit".lower():
        print("Closing console....")
        print("Your score is " + str(user_score) + " and the computer scored " + str(computer_score))
        exit = True

    if user_option == "rock".lower():
        if computer_option == "rock".lower():
            print("Its a tie, you both picked rock")
        elif computer_option == "paper".lower():
            print("computer picked paper and wins this round, you picked rock")
            computer_score += 1
        elif computer_option == "scissors".lower():
            print("you win this round, you picked rock and computer picked scissors")
            user_score += 1
    elif user_option == "paper".lower():
        if computer_option == "rock".lower():
            print("You win this round, you picked paper and computer picked rock")
            user_score += 1
        elif computer_option == "paper".lower():
            print("Its a tie, you both picked paper")
        elif computer_option == "scissors".lower():
            print("computer win this round, you picked paper and computer picked scissors")
            computer_score += 1
    elif user_option == "scissors".lower():
        if computer_option == "rock".lower():
            print("computer win this round, you picked scissors and computer picked rock")
            computer_score += 1
        elif computer_option == "paper".lower():
            print("You win this round, you picked scissors and computer picked paper")
            user_score += 1
        elif computer_option == "scissors".lower():
            print("it's a tie you both picked scissors")
    elif user_option != "rock".lower() or user_option != "paper".lower() or user_option != "scissors".lower():
        print("Invalid input, try inputing either rock, paper, scissors or exit()")