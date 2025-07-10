import asyncio
import uvicorn
from fastapi import FastAPI

from db.base import create_db
from routers.reviews import router as reviews_router


app = FastAPI()
app.include_router(reviews_router)

@app.get("/")
async def root():
    return {"message": "Hello World!"}

if __name__ == "__main__":
    asyncio.run(create_db())
    uvicorn.run(app, host="127.0.0.1", port=8000)
