def bubble_sorting(data):
	for a in range(len(data)):
		for b in range(len(data) - a - 1):
			if data[b] > data[b+1]:
				swap = data[b]
				data[b] = data[b+1]
				data[b+1] = swap
				print(f"   {data}\n")
	print(f"\n\n After Performing BUBBLE Sorting : {data}")


x = [int(x) for x in input("Enter the No with comma to differenciate between them : ").split(",")]

bubble_sorting(x)
