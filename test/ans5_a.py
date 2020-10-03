students = {}

def student_data():
	name = input(" Enter the name of Student : ")
	reg_num = input(" Enter the registration no of Student : ")
	marks = input(" Enter the Total Marks of Student : ")

	students[name] = [reg_num, marks]
	print("\nEntry Added")

def search_data(name):
	if name not in students.keys():
		print("\nStudent not Avalaible")
	else:
		print(f" Student Name is : {name}\n Registration No is : {students[name][0]}\n Total Marks are : {students[name][1]}")

a = True
while a == True:
	chose = int(input("\n 1. Add Data \n 2. Search Data \n 3. EXIT \n\n Choose from above options : "))
	if chose == 1:
		student_data()
	elif chose == 2:
		name = input("\n Enter the Name for search : ")
		search_data(name)
	elif chose == 3:
		break
	else:
		print("\n Wrong Input, Try Again... \n")