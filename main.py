from fastapi import FastAPI
from peewee import *
from datetime import date
DATABASE='tweepee1.db'

database=SqliteDatabase(DATABASE)
class BaseModel(Model):
    class Meta:
        database=database

class User(BaseModel):
    userid=CharField(unique=True)
    password=CharField()
    email=CharField()
    join_date=DateTimeField()

class Post(BaseModel):
    postedBy=ForeignKeyField(User,backref='Post')
    postName=CharField()
    caption=CharField()

    
def create_tables():
    with database:
        database.create_tables([User,Post])

def initialize_db():
    database.connect()
    database.create_tables([User],safe=True)
    database.close()

# if __name__ == "__main__":
#     create_tables()

# post1=Post.create(postedBy=1,postName='post_66',caption='abcdxs')
# post2=Post.create(postedBy=2,postName='post_2',caption='qwe')
# post3=Post.create(postedBy=3,postName='post_3',caption='ert')
# post4=Post.create(postedBy=4,postName='post_4',caption='ery')
# post5=Post.create(postedBy=5,postName='post_5',caption='dfhg')
# user1=User(userid='1',password='123',email='abc@123.com',join_date=date(2021,1,2))
# user1.save()
# user2=User(userid='2',password='223',email='abc@222.com',join_date=date(2022,1,2))
# user2.save()
# user3=User(userid='3',password='333',email='abc@333.com',join_date=date(2024,1,2))
# user3.save()
# user4=User(userid='4',password='444',email='abc@444.com',join_date=date(2025,1,2))
# user4.save()
# user5=User(userid='5',password='555',email='abc@55.com',join_date=date(2026,1,2))
# user5.save()

app =FastAPI()

@app.get("/get_users")#works fine
def get_users_func():
   k=User.select()
   ans=[]
   for i in k:
      ans.append(i)
   return ans

@app.get("/get_single_users/{inputuserid}")#not fine
def get_single_users(inputuserid):
   usersData=User.select().where(User.userid==inputuserid)
   return usersData

@app.get("/get_posts")#works fine
def get_posts():
   post_table=Post.select()
   ans=[]
   for i in post_table:
      ans.append(i)
   return ans

@app.get("/get_posts_userid/{x}")#works fine
def get_posts_userid(x):
  postData=Post.select()
  for i in postData:
   if (i.postedBy.userid==x):
      return i

