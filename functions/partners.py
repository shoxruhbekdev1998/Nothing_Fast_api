from fastapi import HTTPException
from sqlalchemy.orm import joinedload

from models.partners import Partners
from routes.auth import get_password_hash

from utils.pagination import pagination


def all_partners(search, id, from_date, end_date, page, limit, db, status):
    partners = db.query(Partners).options(joinedload(Partners.partner_files)).filter(Partners.id >= 0)
    if search:
         partners= partners.filter(Partners.partner_name.like(search)|
                                   Partners.partner_description.like(search)|
                                   Partners.partner_link.like(search))

    if id:
        partners = partners.filter(Partners.id == id)

    if from_date and end_date:
        partners = partners.filter(Partners.date >= from_date, Partners.date <= end_date)

    if status == True:
        partners = partners.filter(Partners.status == status)

    elif status == False:
        partners = partners.filter(Partners.status == status)

    else:
        partners = partners.filter(Partners.id >= 0)

    return pagination(form=partners, page=page, limit=limit)


def add_partners(partner_name,partner_description,partner_link, db):
    new_partners = Partners(
        partner_name=partner_name,
        partner_description=partner_description,
        partner_link=partner_link,

    )
    db.add(new_partners)
    db.commit()
    db.refresh(new_partners)

    return {"data":new_partners.id }


def update_partners(id, form, db):
    if one_partner(id=form.id, db=db) is None:
        raise HTTPException(status_code=400, detail="Bunday raqamli question yo'q")

    db.query(Partners).filter(Partners.id == id).update({
        Partners.partner_name: form.partner_name,
        Partners.partner_description: form.partner_description,
        Partners.partner_link: form.partner_link,
        Partners.status: form.status,

    })
    db.commit()


def one_partner(id, db):
    return db.query(Partners).filter(Partners.id == id).first()


def delete_partners(id, db):
    db.query(Partners).filter(Partners.id == id).update({
        Partners.status: False
    })

    db.commit()
    return {"data": "Malumot o'chirildi"}
