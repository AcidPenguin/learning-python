import time

def check_number():

	print("Enter a number to identify if it is odd or even")

	num = input()

	if int(num) % 2 == 0:
		print("That is an even number!")
		
	else:
		print("That is an odd number!")


def start():
	quit = False

	while not quit:
		print("Do Another? [Y/n]")

		answ = input()

		if answ.lower().startswith("n"):
			quit = True
		if answ.lower().startswith("y"):
			check_number()

print("Hello, I am the odd even bot.")
print("What is your name?")

name = input()

print("Hello, " + name)

time.sleep(.300)
	
check_number()
start()