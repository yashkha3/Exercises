"""Format Specifiers = Format specifers are used in strings for formating. We also can 
					   say that format specifiers holds position for variables in strings.
					   Python uses C style string formating. Their symbols are %s for string
					   and %d for int and many more. An example is given below :
"""
name = "Yash"
age = 20
print(" Hello I am %s and I am %d years old." % (name, age))

"""But from Python 3.6 we are working with formated string literals or f-string.
   which is an efficent replacement. we want to define the keywords within curley
   braces, into the string. An example is given below : 
"""

print(f"\n Hello I am {name} and I am {age} years old.")


'''Escape Sequence = Escape sequence is sequence of characters that does not represent itself when used. Escape sequence allow us to include special charactes
   as well as responsible to continue a string from a new line. Some of are \' for single quote, \\ this is backslash
   \n for new line \f for form feed and many more. An Example is Given Below :  
'''

print(f"\n\n \'This is officer Python\' \n Reporting from \f v3.8 station")