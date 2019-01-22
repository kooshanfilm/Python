import pymongo
from pymongo.database import Database

from models.post import Post

Database.initialize()
post = Post("pos1","con","au")
post2 = Post("pos2","con2","au2")

print (post2.content)





# url = "mongodb://127.0.0.1:27017"
# client = pymongo.MongoClient(url)
# database = client['fullstack']
# collection = database['students']
#
# students = [student['mark'] for student in collection.find({})]
#
# print (students)
#


