from fastapi import FastAPI
from .routers import  games, filters


app = FastAPI()
app.include_router(games.router)
app.include_router(filters.router)

@app.get("/")
async def root():
    return {"message": "Hello World Again"}