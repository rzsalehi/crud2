import uvicorn
from fastapi import FastAPI
from src.routers.routers import  router
from src.utils.db import init_db

app = FastAPI()

app.include_router(router)

@app.on_event("startup")
def on_startup():
    init_db()


if __name__ == "__main__":
    uvicorn.run(app="main:app", host="0.0.0.0", port=3000, reload=True)
