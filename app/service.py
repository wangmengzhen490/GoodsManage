from sqlalchemy.orm import Session
from .models import Good
from .schemas import GoodsCreate,GoodsUpdate,GoodsRead

class GoodService:
    # 获取商品列表
    @staticmethod
    def get_goods(db:Session,page:int=1,size:int=2):
        skip = (page-1)*size
        q = db.query(Good)
        data = q.offset(skip).limit(size).all()
        total = q.count()
        return {'data':data,'total':total}

    # 单个商品
    @staticmethod
    def get_one_good(db:Session,id:int):
        good = db.query(Good).filter(Good.id == id).first()
        if not good:
            return None
        return good

    # 新增商品
    @staticmethod
    def create_good(db:Session,obj:GoodsCreate):
        good = Good(**obj.model_dump())
        db.add(good)
        db.commit()
        db.refresh(good)
        return good

    # 修改商品
    @staticmethod
    def update_good(db:Session,id:int,obj:GoodsUpdate):
        good = db.query(Good).filter(Good.id == id).first()
        if not good:
            return None
        for k,v in obj.model_dump(exclude_none=True).items():
            setattr(good,k,v)
        db.commit()
        db.refresh(good)
        return good

    # 删除商品
    @staticmethod
    def delete_good(db:Session,id:int):
        good = db.query(Good).filter(Good.id == id).first()
        if not good:
            return None
        db.delete(good)
        db.commit()
        return True

        

