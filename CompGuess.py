#Comp Guess

import time
import sys

def compguess(number):
    low = 1
    high = 100
    guess = 50
    while guess != number:
        guess = (low+high)//2
        
        time.sleep(1)
        print("Hmm.. is it, ", guess)
        if guess > number:
            high = guess
        elif guess < number:
            low = guess + 1

    print("Ah! It's ", guess)

def main():

    name = input("Hello, What's your name?")

    join = input("Nice to meet you " + name + ". Would you like to play a guessing game?")

    
    if join.startswith("y"):
        print("Okay, think of a number between 1 and 100")
    elif join.startswith("n"):
        print("Oh never mind :(")
        sys.exit()
        
    number = 0

    while number < 1 or number > 100:
        number = int(input("Enter a number"))
        if number >100:
            print ("That aint between 1 and 100 tho")
        if number <1:
            print ("That aint between 1 and 100 tho")
        else:
            compguess(number)

main()