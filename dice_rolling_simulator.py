import random

def roll_dice():
    roll = input("Roll dice? (Yes/No): ")

    while roll.lower() == "yes".lower():
        dice_1 = random.randint(1, 6)
        dice_2 = random.randint(1, 6)
        print("dice rolled {} and {}".format(dice_1, dice_2) )
        roll = input("Roll dice again? (Yes/No): ")

roll_dice()