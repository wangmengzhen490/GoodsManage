from pydantic import BaseModel,ConfigDict

class GoodsCreate(BaseModel):
    gname:str
    price:float
    stock:int

class GoodsUpdate(BaseModel):
    gname:str | None = None
    price:float | None = None
    stock:int | None = None

class GoodsRead(GoodsCreate):
    id:int
    model_config = ConfigDict(from_attributes=True)