from pymongo import MongoClient
client = MongoClient('localhost', 27017)  #내컴퓨터에서 돌아가고있는 몽고 디비에 접속
db = client.dbsparta

#insert/ find/ update / delete

db.users.delete_one({'name':'bobby'})