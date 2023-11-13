from fastapi import HTTPException
from sqlalchemy.orm import joinedload

from models.about_services import About_Services

from routes.auth import get_password_hash

from utils.pagination import pagination


def all_about_services(search, id, from_date, end_date, page, limit, db, status):
    about_services = db.query(About_Services).options(joinedload(About_Services.uploaded_files)).filter(About_Services.id >= 0)
    if search:
        about_services = about_services.filter(About_Services.services.like(search) |
                                   About_Services.description.like(search))

    if id:
        about_services = about_services.filter(About_Services.id == id)

    if from_date and end_date:
        about_services = about_services.filter(About_Services.date >= from_date, About_Services.date <= end_date)

    if status == True:
        about_services = about_services.filter(About_Services.status == status)

    elif status == False:
        about_services = about_services.filter(About_Services.status == status)

    else:
        about_services = about_services.filter(About_Services.id >= 0)

    return pagination(form=about_services, page=page, limit=limit)


def add_about_services(services_id,services,description, db):
    new_about_services = About_Services(
        services_id=services_id,
        services=services,
        description=description,

    )
    db.add(new_about_services)
    db.commit()
    db.refresh(new_about_services)

    return {"data": new_about_services.id}


def update_about_services(id, form, db):
    if one_about_service(id=form.id, db=db) is None:
        raise HTTPException(status_code=400, detail="Bunday raqamli question yo'q")

    db.query(About_Services).filter(About_Services.id == id).update({
        About_Services.services_id: form.services_id,
        About_Services.services: form.services,
        About_Services.description: form.description,
        About_Services.status: form.status,

    })
    db.commit()


def one_about_service(id, db):
    return db.query(About_Services).filter(About_Services.id == id).first()


def delete_about_services(id, db):
    db.query(About_Services).filter(About_Services.id == id).update({
        About_Services.status: False
    })

    db.commit()
    return {"data": "Malumot o'chirildi"}
