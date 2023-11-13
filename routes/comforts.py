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
from functions.comforts import *
from schemas.comforts import *

router_comfort = APIRouter()

@router_comfort.post('/add')
def add_comfort(comfort_name: str = File(),
                comfort_description: str = File(None),
                files: typing.Optional[typing.List[UploadFile]] = File(None),db: Session = Depends(get_db),current_user: UserCurrent = Depends(get_current_active_user)):
    comfort_id = add_comforts(comfort_name=comfort_name, comfort_description=comfort_description,db=db)
    if files:
        for file in files:
            with open("media/" + file.filename, 'wb') as image:
                shutil.copyfileobj(file.file, image)
                url = str('media/' + file.filename)
                add_file(url=url, source='comfort', source_id=comfort_id.get('data'), db=db)
        raise HTTPException(status_code=200, detail="Amaliyot muvofaqqiyatli bajarildi")


@router_comfort.get('/',status_code=200)
def get_comfort(search:str=None,id:int=0,from_date:str=None,end_date:str=None,page:int=1,limit:int=5,status:bool=None,db: Session = Depends(get_db),current_user: UserCurrent = Depends(get_current_active_user)):

        return all_comforts(db=db,status=status,search=search,id=id,from_date=from_date,end_date=end_date,page=page,limit=limit)



@router_comfort.put('/update',)
def update_comfort(form:ComfortsUpdate,db: Session = Depends(get_db),current_user: UserCurrent = Depends(get_current_active_user)):

    if update_comforts(id=form.id,form=form,db=db):
        raise HTTPException(status_code=200, detail="Amaliyot muvofaqqiyatli bajarildi")

@router_comfort.delete('/del',)
def delete_comfort(id:int,db: Session = Depends(get_db),current_user: UserCurrent = Depends(get_current_active_user)):
    return delete_comforts(id=id,db=db)