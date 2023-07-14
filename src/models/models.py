from sqlmodel import Field, SQLModel


class Item(SQLModel, table=True):
    __tablename__ = "items"

    id: int = Field(primary_key=True, index=True)
    name: str = Field()
    price: float
