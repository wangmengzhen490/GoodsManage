from fastapi import APIRouter, Depends, HTTPException, Query
from typing import Optional
from sqlalchemy.orm import Session
from .database import get_db
from .schemas import GoodsCreate,GoodsUpdate,GoodsRead
from .service import GoodService
from .dependencies import pagination

router = APIRouter(prefix="/goods")

@router.get("/")
def list_goods(
    db:Session = Depends(get_db),
    pages = Depends(pagination)
):
    return GoodService.get_goods(db,pages["page"],pages["size"])

@router.get("/{id}",response_model=GoodsRead)
def one_good(id:int,db:Session=Depends(get_db)):
    good = GoodService.get_one_good(db,id)
    if not good:
        raise HTTPException(status_code=404,detail="找不到该商品")
    return good

@router.post("/",response_model=GoodsRead,status_code=201)
def add_good(item:GoodsCreate,db:Session=Depends(get_db)):
    return GoodService.create_good(db,item)

@router.put("/{id}",response_model=GoodsRead)
def edit_good(id:int,item:GoodsUpdate,db:Session=Depends(get_db)):
    good = GoodService.update_good(db,id,item)
    if not good:
        raise HTTPException(status_code=404,detail="找不到该商品")
    return good

@router.delete("/{id}")
def del_good(id:int,db:Session=Depends(get_db)):
    ok = GoodService.delete_good(db,id)
    if not ok:
        raise HTTPException(status_code=404,detail="找不到该商品")
    return {"msg":"删除成功"}