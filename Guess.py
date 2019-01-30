#Guess

import random

no_guess = 0

name = input("Hi, What's your name?")

number = random.randint(1,100)
print("Well " + name + " Guess the number I'm thinking of between 1 and 100")

while no_guess < 6:
	print("Take a guess")
	guess = input()
	guess = int(guess)

	no_guess = no_guess + 1

	if guess < number:
		print("Sorry mate, too low")

	if guess > number:
		print("Sorry mate, too high")

	if guess == number:
		break

if guess == number:
	no_guess = str(no_guess)
	print("Sick one, " + name + "! You got it in " + no_guess + " guesses!")

if guess != number:
	number = str(number)
	print("Ay lmao. It was actually " + number)