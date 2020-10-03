string = input("\n\n Enter the sentence : ")
new_string = ""
for s in string:
	if(s.isupper()):
		new_string += s.lower()

	elif(s.islower()):
		new_string += s.upper()

	elif(s.isspace()):
		new_string += s
		

print(f"\n\n {new_string}")
