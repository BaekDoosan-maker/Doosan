client = MongoClient('mongodb+srv://test:sparta@cluster0.9cihgwo.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta

doc = {'name','bobby','age',27}
db.users.insert_one(doc)