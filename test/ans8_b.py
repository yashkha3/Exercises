'''Pickle Module : The Pickle is used for converting data and objects to manner which 
					can be stored to secondary storage devices or shared over network.
					We can say Pickle do seralising and de-seralising and convert data
					to bytes so it can be saved for further operations.
'''

import pickle

stu = {'name' : "Yash Khatri",
		'age' : "20",
		'height' : "5feet 11inch"}

dbfile = open('myinfo', 'ab')
pickle.dump(stu, dbfile)

dbfile.close()

# continue with cont.py in directory




