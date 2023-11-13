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
from functions.about_services import *
from schemas.about_services import *

router_about_servic = APIRouter()

@router_about_servic.post('/add')
def add_about_servic(services: str = File(),
                services_id: int = File(),
                description: str = File(None),
                files: typing.Optional[typing.List[UploadFile]] = File(None),db: Session = Depends(get_db),current_user: UserCurrent = Depends(get_current_active_user)):

    about_servic_id = add_about_services(services=services, services_id=services_id,  description=description,db=db)
    if files:
        for file in files:
            with open("media/" + file.filename, 'wb') as image:
                shutil.copyfileobj(file.file, image)
                url = str('media/' + file.filename)
                add_file(url=url, source='about_servic', source_id=about_servic_id.get('data'), db=db)
        raise HTTPException(status_code=200, detail="Amaliyot muvofaqqiyatli bajarildi")

@router_about_servic.get('/',status_code=200)
def get_about_servic(search:str=None,id:int=0,from_date:str=None,end_date:str=None,page:int=1,limit:int=5,status:bool=None,db: Session = Depends(get_db),current_user: UserCurrent = Depends(get_current_active_user)):

        return all_about_services(db=db,status=status,search=search,id=id,from_date=from_date,end_date=end_date,page=page,limit=limit)



@router_about_servic.put('/update',)
def update_about_servic(form:About_ServicesUpdate,db: Session = Depends(get_db),current_user: UserCurrent = Depends(get_current_active_user)):

    if update_about_servic(id=form.id,form=form,db=db):
        raise HTTPException(status_code=200, detail="Amaliyot muvofaqqiyatli bajarildi")

@router_about_servic.delete('/del',)
def delete_about_servic(id:int,db: Session = Depends(get_db),current_user: UserCurrent = Depends(get_current_active_user)):
    return delete_about_services(id=id,db=db)