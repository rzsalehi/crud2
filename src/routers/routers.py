from fastapi import Depends, APIRouter
from src.utils.db import *
from src.models.models import *
from src.schemas.schema import ItemIn

router = APIRouter(prefix="/api")

@router.get("/healthy")
def pong():
    return {"status": "yes"}


@router.post("/insert")
def insrec(args : ItemIn =Depends(ItemIn), session: Session = Depends(get_session)):
    item = Item(name=args.name, price=args.price)
    session.add(item)
    session.commit()

    return {"msg": "success"}

