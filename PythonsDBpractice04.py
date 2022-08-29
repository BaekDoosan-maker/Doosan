from pymongo import MongoClient

from hello import soup

client = MongoClient('mongodb+srv://test:sparta@cluster0.9cihgwo.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta


movie = db.movies.find_one({'title':'가버나움'})
star = movie['star']

all_movies = list(db.movies.find({'star':star},{'_id':False}))

for m in all_movies:
    print(m['title'])





