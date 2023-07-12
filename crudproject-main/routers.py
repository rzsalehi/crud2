from fastapi import FastAPI, Depends
from db import init_db,get_session
from sqlmodel import Session
from models import *
import uvicorn
from schema import ItemIn



app= FastAPI()


@app.on_event("startup")
def on_startup():
    init_db()


@app.get("/healthy")
def pong():
    return {"status": "yes"}


@app.post("/insert")
def insrec(args : ItemIn =Depends(ItemIn), session: Session = Depends(get_session)):
    item = Item(name=args.name, price=args.price)
    session.add(item)
    session.commit()

    return {"msg": "success"}

if __name__ == "__main__":
    uvicorn.run(app="routers:app", host="0.0.0.0", port=3000, reload=True)
