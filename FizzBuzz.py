#FizzBuzz


for n in range(1,100):
	
	t = (n % 3 == 0)
	te = (n % 10 == 0)
	
		
	if te and t:
		print("FizzBuzz")
	
	elif t:
		print("Fizz")
 	
	elif te:
		print("Buzz")

	else: 
		print(str(n))