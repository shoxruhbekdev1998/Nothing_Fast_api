import shutil
import typing

from fastapi import APIRouter, Depends, HTTPException, UploadFile, File
from pydantic.datetime_parse import date

from db import Base,engine,get_db

from sqlalchemy.orm import Session

from functions.files import add_file
from routes.auth import get_current_active_user
from schemas.users import UserCurrent

Base.metadata.create_all(bind=engine)
from functions.partners import *
from schemas.partners import *

router_partner = APIRouter()

@router_partner.post('/add')
def add_partner(partner_name: str = File(),
                partner_description : str = File(None),
                partner_link: str = File(None),
                files: typing.Optional[typing.List[UploadFile]] = File(None),db: Session = Depends(get_db),current_user: UserCurrent = Depends(get_current_active_user)):
    partner_id = add_partners(partner_name=partner_name, partner_description=partner_description, partner_link=partner_link, db=db)
    if files:
        for file in files:
            with open("media/" + file.filename, 'wb') as image:
                shutil.copyfileobj(file.file, image)
                url = str('media/' + file.filename)
                add_file(url=url, source='partner', source_id=partner_id.get('data'), db=db)
        raise HTTPException(status_code=200, detail="Amaliyot muvofaqqiyatli bajarildi")




@router_partner.get('/',status_code=200)
def get_partner(search:str=None,id:int=0,from_date:str=None,end_date:str=None,page:int=1,limit:int=5,status:bool=None,db: Session = Depends(get_db),current_user: UserCurrent = Depends(get_current_active_user)):

        return all_partners(db=db,status=status,search=search,id=id,from_date=from_date,end_date=end_date,page=page,limit=limit)



@router_partner.put('/update',)
def update_partner(form:PartnersUpdate,db: Session = Depends(get_db),current_user: UserCurrent = Depends(get_current_active_user)):

    if update_partners(id=form.id,form=form,db=db):
        raise HTTPException(status_code=200, detail="Amaliyot muvofaqqiyatli bajarildi")

@router_partner.delete('/del',)
def delete_partner(id:int,db: Session = Depends(get_db),current_user: UserCurrent = Depends(get_current_active_user)):
    return delete_partners(id=id,db=db)