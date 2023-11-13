from fastapi import HTTPException
from sqlalchemy.orm import joinedload

from models.services import Services
from routes.auth import get_password_hash

from utils.pagination import pagination


def all_services(search, id, from_date, end_date, page, limit, db, status):
    services = db.query(Services).options(joinedload(Services.about_servic)).filter(Services.id >= 0)
    if search:
         services= services.filter(Services.services_names.like(search))

    if id:
        services = services.filter(Services.id == id)

    if from_date and end_date:
        services = services.filter(Services.date >= from_date, Services.date <= end_date)

    if status == True:
        services = services.filter(Services.status == status)

    elif status == False:
        services = services.filter(Services.status == status)

    else:
        services = services.filter(Services.id >= 0)

    return pagination(form=services, page=page, limit=limit)


def add_services(form, db):
    new_services = Services(
        services_names=form.services_names,
        )
    db.add(new_services)
    db.commit()
    db.refresh(new_services)

    return {"data": "Services add base"}


def update_services(id, form, db):
    if one_servic(id=form.id, db=db) is None:
        raise HTTPException(status_code=400, detail="Bunday raqamli question yo'q")

    db.query(Services).filter(Services.id == id).update({
        Services.services_names: form.services_names,
        Services.status: form.status,

    })
    db.commit()


def one_servic(id, db):
    return db.query(Services).filter(Services.id == id).first()


def delete_services(id, db):
    db.query(Services).filter(Services.id == id).update({
        Services.status: False
    })

    db.commit()
    return {"data": "Malumot o'chirildi"}
