def lin_search(num_list, search):
	for i in range(len(num_list)):
		if num_list[i] == search:
			return True
	return False

num_list = [6,2,37,5,8,12,17,21,27,35,50,97,88,99,100]
print(f" Items in list : {num_list}")

search = int(input("\n\n Enter the no to search from list : "))
if lin_search(num_list, search):
	print("True")

else:
	print("False")
