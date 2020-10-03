string = input("\n\n Enter the sentence : ")
d = a = w = u = l = 0

w = len(string.split())

for s in string:
	if(s.isupper()):
		u = u+1

	elif(s.islower()):
		l = l+1
		
	elif s.isdigit():
		d = d+1

	elif s.isalpha():
		a = a+1

print(f"\n\n Words : {w}\n Digits : {d}\n Alphabets : {a}\n Uppercase : {u}\n Lowercase : {l} ")
