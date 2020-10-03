import pickle
file = open('myinfo', 'rb')
db = pickle.load(file)
print(db) 
