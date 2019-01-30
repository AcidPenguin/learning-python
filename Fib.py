# Fib

#Number of Fibonacci terms
numfib = 10

#first two terms
n1 = 0
n2 = 1
count = 0

#check if the number of fib terms is valid

if numfib <= 0:
	print("make your integer bigger than 0, you tit")
else :
	print("Fibonacci sequence upto" ,numfib, ":")
	while count < numfib:
		print(n1,end=' , ')
		nth = n1 + n2
		#update values
		n1 = n2
		n2 = nth
		count += 1

print("\n")