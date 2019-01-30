import time

print("Hello, I am the odd even bot.")

time.sleep(.300)

print("What is your name?")

name = input()

print ("Hello " + name + ", please enter a number and I will tell you if it is odd or even.")

num = input()

if int(num)%2 == 0:
		
	print("That is an even number!")

else:
		
	print("That is an odd number!")
