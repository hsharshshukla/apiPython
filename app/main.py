from fastapi import FastAPI,status
from fastapi.middleware.cors import CORSMiddleware
from . import models
from .database import engine
from .routers import post,user,auth,vote
from .config import settings


#Below line auto generated tables in db as per models on reload
# models.Base.metadata.create_all(bind= engine)

app = FastAPI()

# origins =["http://localhost:8000"]
origins =["*"]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)

@app.get("/",status_code=status.HTTP_200_OK)
def root():
    return {"message":"Home Page"}