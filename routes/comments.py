import shutil
import typing

from fastapi import APIRouter, Depends, HTTPException, File, UploadFile
from pydantic.datetime_parse import date

from db import Base,engine,get_db

from sqlalchemy.orm import Session

from functions.files import add_file
from routes.auth import get_current_active_user
from schemas.users import UserCurrent

Base.metadata.create_all(bind=engine)
from functions.comments import *
from schemas.comments import *

router_comment = APIRouter()

@router_comment.post('/add')
def add_comment( name: str = File(),
                 last_name: str = File(None),
                 comment: str = File(None),

                 files: typing.Optional[typing.List[UploadFile]] = File(None),db: Session = Depends(get_db),current_user: UserCurrent = Depends(get_current_active_user)):
    comment_id = add_comments(name=name, last_name=last_name,comment=comment, db=db)
    if files:
        for file in files:
            with open("media/" + file.filename, 'wb') as image:
                shutil.copyfileobj(file.file, image)
                url = str('media/' + file.filename)
                add_file(url=url, source='comment', source_id=comment_id.get('data'), db=db)
        raise HTTPException(status_code=200, detail="Amaliyot muvofaqqiyatli bajarildi")

@router_comment.get('/',status_code=200)
def get_comment(search:str=None,id:int=0,from_date:str=None,end_date:str=None,page:int=1,limit:int=5,status:bool=None,db: Session = Depends(get_db),current_user: UserCurrent = Depends(get_current_active_user)):

        return all_comments(db=db,status=status,search=search,id=id,from_date=from_date,end_date=end_date,page=page,limit=limit)



@router_comment.put('/update',)
def update_comment(form:CommentsUpdate,db: Session = Depends(get_db),current_user: UserCurrent = Depends(get_current_active_user)):

    if update_comments(id=form.id,form=form,db=db):
        raise HTTPException(status_code=200, detail="Amaliyot muvofaqqiyatli bajarildi")

@router_comment.delete('/del',)
def delete_comment(id:int,db: Session = Depends(get_db),current_user: UserCurrent = Depends(get_current_active_user)):
    return delete_comments(id=id,db=db)