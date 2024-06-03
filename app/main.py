from fastapi import FastAPI
from routers import stories, users
from database import engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(stories.router)
app.include_router(users.router)

@app.get("/")
def read_root():
    return {"message": "deu certo"}
