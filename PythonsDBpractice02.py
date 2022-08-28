from pymongo import MongoClient
client = MongoClient('mongodb+srv://test:sparta@cluster0.9cihgwo.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta

all_users = list(db.users.find({},{'_id':False}))

for user in all_users:
    print(user)

user = db.users.find_one({'name':'bobby'})
print(user['age'])

