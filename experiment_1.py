stu_data = [{'name' : "yash", 'mobile' : "9144818318"},	
			{'name' : "arpan", 'mobile' : "9898123456"},	
			{'name' : "bhagwati", 'mobile' : "9898564321"},	
			{'name' : "bhavya", 'mobile' : "6262185143"},	
			{'name' : "chetan", 'mobile' : "7869198400"},	
			{'name' : "karuppasamy", 'mobile' : "8989404424"},	
			{'name' : "parv", 'mobile' : "7987537578"},	
			{'name' : "rahul.s", 'mobile' : "9236885790"},	
			{'name' : "rahul.u", 'mobile' : "8246907533"},	
			{'name' : "shikha", 'mobile' : "7358974455"},	
			{'name' : "shubh", 'mobile' : "6234567565"},	
			{'name' : "tulsiram", 'mobile' : "9324456757"},	
			{'name' : "yogesh", 'mobile' : "8945234233"} 
			]

name = input('Enter the name : ')

for i in stu_data:
	if i['name'] == name:
		print(f"The mobile no you have asked for { i['name'] } is +91 { i['mobile']} ENJOY :-))")
		break
	elif name == "":
		print("yow didnt write anything")
		break
else:
	print("nothing found in this dict :-((")

input('Press ENTER to exit')
		


	


		



