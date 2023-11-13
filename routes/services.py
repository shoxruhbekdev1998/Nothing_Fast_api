from fastapi import APIRouter,Depends,HTTPException
from pydantic.datetime_parse import date

from db import Base,engine,get_db

from sqlalchemy.orm import Session

from routes.auth import get_current_active_user
from schemas.users import UserCurrent

Base.metadata.create_all(bind=engine)
from functions.services import *
from schemas.services import *

router_servic = APIRouter()

@router_servic.post('/add')
def add_servic(form:ServicesCreate,db: Session = Depends(get_db),current_user: UserCurrent = Depends(get_current_active_user)):

    if add_services(form=form,db=db):
        raise HTTPException(status_code=200, detail="Amaliyot muvofaqqiyatli bajarildi")


@router_servic.get('/',status_code=200)
def get_servic(search:str=None,id:int=0,from_date:str=None,end_date:str=None,page:int=1,limit:int=5,status:bool=None,db: Session = Depends(get_db),current_user: UserCurrent = Depends(get_current_active_user)):

        return all_services(db=db,status=status,search=search,id=id,from_date=from_date,end_date=end_date,page=page,limit=limit)



@router_servic.put('/update',)
def update_servic(form:ServicesUpdate,db: Session = Depends(get_db),current_user: UserCurrent = Depends(get_current_active_user)):

    if update_services(id=form.id,form=form,db=db):
        raise HTTPException(status_code=200, detail="Amaliyot muvofaqqiyatli bajarildi")

@router_servic.delete('/del',)
def delete_servic(id:int,db: Session = Depends(get_db),current_user: UserCurrent = Depends(get_current_active_user)):
    return delete_services(id=id,db=db)