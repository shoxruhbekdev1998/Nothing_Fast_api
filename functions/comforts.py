from fastapi import HTTPException
from sqlalchemy.orm import joinedload

from models.comforts import Comforts

from routes.auth import get_password_hash

from utils.pagination import pagination


def all_comforts(search, id, from_date, end_date, page, limit, db, status):
    comforts = db.query(Comforts).options(joinedload(Comforts.comfort_files)).filter(Comforts.id >= 0)
    if search:
         comforts= comforts.filter(Comforts.comfort_name.like(search)|
                                   Comforts.comfort_description.like(search))

    if id:
        comforts = comforts.filter(Comforts.id == id)

    if from_date and end_date:
        comforts = comforts.filter(Comforts.date >= from_date, Comforts.date <= end_date)

    if status == True:
        comforts = comforts.filter(Comforts.status == status)

    elif status == False:
        comforts = comforts.filter(Comforts.status == status)

    else:
        comforts = comforts.filter(Comforts.id >= 0)

    return pagination(form=comforts, page=page, limit=limit)


def add_comforts(comfort_name,comfort_description, db):
    new_comforts = Comforts(
        comfort_name=comfort_name,
        comfort_description=comfort_description,


    )
    db.add(new_comforts)
    db.commit()
    db.refresh(new_comforts)

    return {"data": new_comforts.id}


def update_comforts(id, form, db):
    if one_comfort(id=form.id, db=db) is None:
        raise HTTPException(status_code=400, detail="Bunday raqamli question yo'q")

    db.query(Comforts).filter(Comforts.id == id).update({
        Comforts.comfort_name: form.comfort_name,
        Comforts.comfort_description: form.comfort_description,
        Comforts.status: form.status,

    })
    db.commit()


def one_comfort(id, db):
    return db.query(Comforts).filter(Comforts.id == id).first()


def delete_comforts(id, db):
    db.query(Comforts).filter(Comforts.id == id).update({
        Comforts.status: False
    })

    db.commit()
    return {"data": "Malumot o'chirildi"}
