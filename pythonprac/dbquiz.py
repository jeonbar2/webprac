from pymongo import MongoClient
client = MongoClient('localhost', 27017)  #내컴퓨터에서 돌아가고있는 몽고 디비에 접속
db = client.dbsparta


movie = db.movies.find_one({'title':'매트릭스'})
target_star = movie['star']
print(target_star)

target_movies = list(db.movies.find({'star':target_star}))
for target in target_movies:
    print(target['title'])

db.movies.update_one({'title':'매트릭스'},{'$set':{'star':'0'}})
