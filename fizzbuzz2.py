'''
fizzbuzz.py
Program lists numbers 1 to 100 but replaces 
multiples of 3 with "Fizz", multiples of 5 
with "Buzz" and multiples of both with "FizzBuzz"
'''

for n in range(1,100):

	t = (n % 3 == 0)
	#t = multiple of 3
	te = (n % 10 == 0)
	#te = multiple of 5