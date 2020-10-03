stack = []

	

a = True
while a == True:
	i = int(input("\n\n 1. PUSH \n 2. POP \n 3. VIEW \n 4. CLEAR \n 5. STOP \n\n\n Choose the operations to process on stack : "))
	if i == 1:
		val = input("\n\n Enter the Value : ")
		stack.append(val)

	elif i == 2:
		stack.pop()

	elif i == 3:
		print("\n". join(stack))

	elif i == 4:
		stack.clear()

	elif i == 5:
		break
