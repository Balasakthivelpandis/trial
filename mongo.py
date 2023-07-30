import pymongo

myclient = pymongo.MongoClient("mongodb+srv://balasakthivelpandi:bala123@cloudmongodb.bxyay8l.mongodb.net/")

mydb = myclient["mydatabase"]
