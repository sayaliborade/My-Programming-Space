word = input("Enter the string for palindrome check:")

if word[:]==word[::-1]:
	print("{0} is a palindrome".format(word))
else:
	print("{0} is not a palindrome".format(word))