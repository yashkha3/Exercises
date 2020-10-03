x = int(input("Enter x value: "))
y = int(input("Enter y value: "))

if(x > 0 and y > 0):
	print("It is in First Quadrant")

elif(x < 0 and y > 0):
	print("It is in Second Quadrant")

elif(x < 0 and y < 0):
	print("It is in Third Quadrant")

elif(x > 0 and y < 0):
	print("It is in Fourth Quadrant")

else:
	print("Kindly Try Again")