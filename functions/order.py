from fastapi import HTTPException
from sqlalchemy.orm import joinedload

from models.order import Orders
from routes.auth import get_password_hash

from utils.pagination import pagination


def all_orders(search, id, from_date, end_date, page, limit, db, status):
    orders = db.query(Orders).filter(Orders.id >= 0)
    if search:
         orders= orders.filter(Orders.name.like(search)|
                                   Orders.email.like(search)|
                                   Orders.phone_number.like(search))

    if id:
        orders = orders.filter(Orders.id == id)

    if from_date and end_date:
        orders = orders.filter(Orders.date >= from_date, Orders.date <= end_date)

    if status == True:
        orders = orders.filter(Orders.status == status)

    elif status == False:
        orders = orders.filter(Orders.status == status)

    else:
        orders = orders.filter(Orders.id >= 0)

    return pagination(form=orders, page=page, limit=limit)


def add_orders(form, db):
    new_orders = Orders(
        name=form.name,
        email=form.email,
        phone_number=form.phone_number,

    )
    db.add(new_orders)
    db.commit()
    db.refresh(new_orders)

    return {"data": "order add base"}


def update_orders(id, form, db):
    if one_order(id=form.id, db=db) is None:
        raise HTTPException(status_code=400, detail="Bunday raqamli question yo'q")

    db.query(Orders).filter(Orders.id == id).update({
        Orders.name: form.name,
        Orders.email: form.email,
        Orders.phone_number: form.phone_number,
        Orders.status: form.status,

    })
    db.commit()


def one_order(id, db):
    return db.query(Orders).filter(Orders.id == id).first()


def delete_orders(id, db):
    db.query(Orders).filter(Orders.id == id).update({
        Orders.status: False
    })

    db.commit()
    return {"data": "Malumot o'chirildi"}
