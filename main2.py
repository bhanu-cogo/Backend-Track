from fastapi import FastAPI
from peewee import *
from datetime import date
DATABASE='tweepee2.db'

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
    no_of_likes=int()
    
class Like(BaseModel):
    userid=ForeignKeyField(User,backref='Post')
    postid=ForeignKeyField(Post,backref='user')
    no_of_likes=int()

def create_tables():
    with database:
        database.create_tables([User,Post])

def initialize_db():
    database.connect()
    database.create_tables([User],safe=True)
    database.close()

if __name__ == "__main__":
    create_tables()
#post table
post1=Post.create(postedBy=1,postName='post_66',caption='abcdxs',no_of_likes=0)
post2=Post.create(postedBy=2,postName='post_2',caption='qwe',no_of_likes=0)
post3=Post.create(postedBy=3,postName='post_3',caption='ert',no_of_likes=0)
post4=Post.create(postedBy=4,postName='post_4',caption='ery',no_of_likes=0)
post5=Post.create(postedBy=5,postName='post_5',caption='dfhg',no_of_likes=0)

#user table
user1=User.create(userid='1',password='123',email='abc@123.com',join_date=date(2021,1,2))
user2=User.create(userid='2',password='223',email='abc@222.com',join_date=date(2022,1,2))
user3=User.create(userid='3',password='333',email='abc@333.com',join_date=date(2024,1,2))
user4=User.create(userid='4',password='444',email='abc@444.com',join_date=date(2025,1,2))
user5=User.create(userid='5',password='555',email='abc@55.com',join_date=date(2026,1,2))
#like table
like=Like.create(userid='1',postedby='2',no_of_likes='20')


app =FastAPI()

@app.get("/get_users")
def get_users_func():
   k=User.select()
   ans=[]
   for i in k:
      ans.append(i)
   return ans

@app.get("/get_single_users/{inputuserid}")
def get_single_users(inputuserid):
   usersData=User.select().where(User.userid==inputuserid)
   return usersData

@app.get("/get_posts")
def get_posts():
   post_table=Post.select()
   ans=[]
   for i in post_table:
      ans.append(i)
   return ans

@app.get("/get_posts_userid/{x}")
def get_posts_userid(x):
  postData=Post.select()
  for i in postData:
   if (i.postedBy.userid==x):
      return i


@app.put("/liked/{inppostid}")
def post_like(inppostid):
    post=Like.select()
    for i in post:
        if i.postedby==int(inppostid):
            print(i.no_of_likes)
            i.no_of_likes=i.no_of_likes+1
            i.save()
    return {"post":"liked"}

@app.put("/disliked/{inppostid}")
def post_dislike(inppostid):
    post=Like.select()
    for i in post:
        if i.postedby==int(inppostid):
            print(i.no_of_likes)
            i.no_of_likes=i.no_of_likes-1
            i.save()
    return {"post":"disliked"}

@app.get("/deleted/{x}")
def deleted_posts(x):
    query = Post.delete().where(Post.postid == int(x))
    query.execute()
    return {"Post": "Deleted"}

@app.get("/searchUsername/{username_tofind}")
def search_username(username_tofind):
    userData=User.get(User.userid==username_tofind)
    return userData


