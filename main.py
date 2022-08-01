import pymongo
client = pymongo.MongoClient("mongodb+srv://hilalpv:muI1NfgMDYq3LeoR@cluster0.eigpleu.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)