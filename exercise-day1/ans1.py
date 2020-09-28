no = []

for a in range(2000, 3200):
	if (a % 7 == 0) and (a % 5 == 0):
		no.append(str(a))
		
print("\n")
print(",". join(no))
