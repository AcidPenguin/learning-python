#Comp Guess

import time
import sys

def compguess():
    low = 1
    high = 100
    guess = 50
    correct = False

    while not correct:
        guess = (low+high)//2
        
        time.sleep(0.2)
        response = input("Hmm.. is it, " + str(guess))

        if "low" in response:
            low = guess
        elif "high" in response:
            high = guess + 1
        elif "correct" in response:
            correct = True

    if correct == True:
        print("Yay I win!")

def main():

    name = input("Hello, What's your name?")

    join = input("Nice to meet you " + name + ". Would you like to play a guessing game?")
    
    if join.startswith("y"):
        print("Okay, think of a number between 1 and 100")
        time.sleep(0.2)
    elif join.startswith("n"):
        print("Oh never mind :(")
        sys.exit()
        #return 0

    compguess()

main()