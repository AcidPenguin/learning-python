#Comp Guess

import time
import sys

def compguess():
    low = 1
    high = 100
    guess = 50
    correct = False
    end = False

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
        elif "exit" in response:
            end = True


    if correct == True:
        print("Yay I win!")
    if end == True:
        exit()

def main():

    name = input("Hello, What's your name?")

    join = input("Nice to meet you " + name + ". Would you like to play a guessing game?")
    
    if join.startswith("y" or "Y"):
        print("Okay, think of a number between 1 and 100 and then tell me if my guess is low, high or correct")
        time.sleep(0.2)
    elif join.startswith("n" or "N"):
        print("Oh never mind :(")
        sys.exit()
        #return 0

    compguess()

main()