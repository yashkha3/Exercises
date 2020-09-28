row_n = int(input("Enter the No of rows : "))
col_n = int(input("Enter the No of colums : "))

array = [[0 for col in range(col_n)] for row in range(row_n)]


for row in range(row_n):
	for col in range(col_n):
		array[row][col] = row * col

print(array)