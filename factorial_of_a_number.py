num = int(input("Enter the number whose factorial you want to find:"))
i = num
factorial = 1

while i > 1:
	factorial = factorial * i
	i = i- 1

print("Factorial of {0} is {1}".format(num,factorial))	 