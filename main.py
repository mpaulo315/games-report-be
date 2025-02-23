from fastapi import FastAPI
from .routers import  games

app = FastAPI()
app.include_router(games.router)

@app.get("/")
async def root():
    return {"message": "Hello World Again"}