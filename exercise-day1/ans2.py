def factorial(num):
	if num == 1:
		return num
	else:
		return num * factorial(num-1)

num = int(input("\nEnter the no : "))
print(f"\n The factorial of {num} is = {factorial(num)}.")
