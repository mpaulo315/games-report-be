from fastapi import FastAPI
from fastapi.middleware.gzip import GZipMiddleware
from .routers import  games, filters


app = FastAPI()

# app.add_middleware(HTTPSRedirectMiddleware)
app.add_middleware(GZipMiddleware, minimum_size=1000, compresslevel=5)

app.include_router(games.router)
app.include_router(filters.router)

@app.get("/")
async def root():
    return {"message": "Hello World Again"}