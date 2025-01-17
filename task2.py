"""
Task 2:
Create a program to play a number guessing game
There should be a function:
title()
displays instructions and how to play

game()
plays the games
"""
import random
import os
import time
def title():
    os.system('cls')
    print("Welcome to number guesser!")
    time.sleep(2.5)
    os.system('cls')
    print("The computer will generate a random number.")
    time.sleep(2.5)
    os.system('cls')
    print("You will have 3 chances to guess it.")
    time.sleep(2.5)
    os.system('cls')
    print("For each incorrect guess you will get a hint.")
    time.sleep(3.5)
    os.system('cls')

def game():
    n = random.randint(0,100)
    #print(n)
    inp = False
    for i in range(1,4):
        while inp == False:
            time.sleep(1)
            os.system('cls')
            try:
                guess = int(input("Guess a number between 1 and 100: "))
            except:
                continue
            if guess > 0 and guess < 100:
                break
        if guess == n:
            print("Congrats! You guessed correct!")
            break
        elif i == 1:
            if n %2 == 0:
                print("The number is even.")
            else: 
                print("The number is odd")
        elif i == 2:
            if guess > n:
                print("The number is less than your guess")
            elif guess < n:
                print("The number is greater than your guess")
        elif i == 3: 
            print("You have use up all your guesses")
            print(f"The number was {n}")



    
    
    

title()

for i in range(100000):
    game()
    time.sleep(3)
    os.system('cls')
    play = input("Play again? Yes/No: ")
    if play == "Yes" or play == "yes":
        pass
    else:
        exit()