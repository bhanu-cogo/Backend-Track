from fastapi import FastAPI, Depends, Header, HTTPException
from fastapi.security import OAuth2PasswordBearer
from peewee import *
from pydantic import BaseModel, validator
import bcrypt

app = FastAPI()
db = SqliteDatabase('my_database.db')
db = SqliteDatabase("posts.db")

class User(Model):
    username = CharField()
    password = CharField()

class Authentication(Model):
    username = CharField()
    password = CharField()

class token_table(Model):
    ses_token=CharField()
    username=ForeignKeyField(User,backref='token_table')
#post username like
class Post(Model):
    postid=CharField()
    likes=int()
    username=ForeignKeyField(User,backref='authentication')
class Meta:
    database = db
    
db.create_tables([Authentication], safe=True)
db.create_tables([token_table], safe=True)
db.create_tables([Post], safe=True)
#User.create(username='bhanu1', password='123456')
Post.create(postid='1',likes='24',username=[])
def hash_password(password: str):
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password.decode('utf-8')
def verify_password(password: str, hashed_password: str):
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8'))

@app.get('/register')
async def add_user_and_get_token(username:str=Header(None),password:str=Header(None)):
    hashed_password = hash_password(password)
    Authentication.create(username=username, password=hashed_password)
    token_table.create(ses_token=username+'session_token',username=username)
    if username is None and password is None:
        return HTTPException(status_code=403, detail="information missing! try Again")
    return "session_token"

@app.post('/users')

@app.get('/posts')
def get_post():
    posts=[]
    for p in Post.select().join(User):
        posts.append(
            { 
                "id": Post.id,
            "username": {
                "username": Post.username
            },
            "likes": Post.likes
            }
        )




