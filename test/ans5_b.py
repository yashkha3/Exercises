# Pre-Defined Dictionary
stu = {'name' : "Yash Khatri",
		'age' : "20",
		'height' : "5feet 11inch"}

# a) get() : Get is a method which return the value of the key ehich is provided to it.. Ex :

print(f"\n Student Name: {stu.get('name')}")

# b) keys() : Keys is a method which is used to view the keys of Dict.. Ex :

print(stu.keys())

# c) pop() : Pop is method which removes an element of which key is provided.. Ex :

whoo = stu.pop('height')
print(f"\n Removed element is : {whoo} \n Updated dictionary : {stu}")

# d) update() : Update method is used to add elements to dictomary.. Ex :

u = {'hobby': "Watching Movies"}
stu.update(u)
print(f"\n\n Updated Element in Dict : {stu}")

# e) values() : Value is a method which is used to view the list of values from Dict.. Ex :

print(f"\n\n {stu.values()}")

# f) items() : Items is a method which is used to display the key and its value from a given dict.. Ex :

print(f"\n\n {stu.items()}") # which shows as tuples in which ('key', 'value')