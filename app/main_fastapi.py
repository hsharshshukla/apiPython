from fastapi import FastAPI,Response,status,HTTPException
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional
from random import randrange
import psycopg2
import time
from psycopg2.extras import RealDictCursor

app = FastAPI()
#Notes
#first path operation matching the request is served


class Post(BaseModel):
    title: str
    content: str 
    published: bool = True   

#DB Connection Setting
while True:
    try:
        conn = psycopg2.connect(host='localhost',
                                database='fastapiDB',
                                user='postgres',
                                password='harsh',
                                cursor_factory=RealDictCursor)
        cursor = conn.cursor()
        print("Database Connection Successfull")
        break
    except Exception as error:
        print("Connecting to database failed!")
        print("Error: ",error)
        time.sleep(2)

my_posts=[{"title":"post1","content":"content of post1","id":1},
          {"title":"post2","content":"content of post2","id":2}]

def find_post(id):
    for p in my_posts:
        if p["id"] == id:
            return p

def find_index_post(id):
    for i,p in enumerate(my_posts):
        if p['id'] == id:
            return i

@app.get("/")
def root():
    return{"message":"Hello World"}

@app.get("/posts")
def get_posts():
    cursor.execute("""Select * from posts""")
    posts = cursor.fetchall()
    return {"data":posts}

@app.post("/posts",status_code=status.HTTP_201_CREATED)
def create_posts(post : Post):
    # cursor.execute("""insert into posts values({post.title},{post.content},{post.published})""") prone to SQL injection attack
    # below code sanitizes input and avoid sql injection attack
    cursor.execute("""insert into posts (title,content,published) values(%s,%s,%s) RETURNING *""",(post.title,post.content,post.published))
    new_post = cursor.fetchone()
    conn.commit()
    return {"data": new_post}

@app.get("/posts/latest")
def get_latest_post():
    cursor.execute("""select * from posts order by id desc limit 1""")
    latest_post = cursor.fetchone()
    return {"detail": latest_post}

@app.get("/posts/{id}")
def get_post(id: int, response: Response):
    # int is coded as below tuple or convert it to str like (str(id))
    cursor.execute("""select * from posts where id = %s""",(id,))
    post = cursor.fetchone()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id: {id} was not found")
    return {"Post Details": post}


@app.delete("/posts/{id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_posts(id:int):
    cursor.execute("""delete from posts where id= %s returning *""",(id,))
    deleted_post =cursor.fetchone()
    conn.commit()

    if deleted_post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id: {id} does not exists") 
    
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@app.put("/posts/{id}")
def update_post(id: int, post : Post):
    cursor.execute("""update posts set title = %s,content = %s, published=%s where id = %s returning * """,
                    (post.title,post.content,post.published,id))
    updated_post = cursor.fetchone()
    conn.commit()

    if updated_post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id: {id} does not exists") 
    
    return {"message":"post udpated"}