from fastapi import HTTPException

from models.users import Users
from routes.auth import get_password_hash
from utils.pagination import pagination


def all_users(search,id,from_date,end_date,page,limit,db,status):
    users = db.query(Users).filter(Users.id >= 0)
    if search:
         users = users.filter(Users.roll.like(search) |
                                   Users.name.like(search) |
                                   Users.last_name.like(search) |
                                   Users.phone_number.like(search))

    if id:
        users = users.filter(Users.id==id)

    if from_date and end_date:
        users = users.filter(Users.date >= from_date, Users.date <= end_date)

    if status == True:
     users = users.filter(Users.status==status)

    elif status == False:
     users = users.filter(Users.status==status)

    else:
        users = users.filter(Users.id>=0)

    return pagination(form=users, page=page, limit=limit)



def add_users(form,db):
    new_user=Users(name=form.name,
                   roll=form.roll,
                   last_name=form.last_name,
                   middle_name=form.middle_name,
                   phone_number=form.phone_number,
                   region=form.region,
                   city=form.city,
                   village=form.village,
                   home_number=form.home_number,
                   birth_day=form.birth_day,
                   username=form.username,
                   password=get_password_hash(form.password)
                   )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return{"data" : "User add base"}

def update_users(id,form,db):
    if one_user(id=form.id,db=db) is None:
        raise HTTPException(status_code=400,detail="Bunday raqamli user mavjud emas qayta urining")
    db.query(Users).filter(Users.id==id).update({
        Users.roll: form.roll,
        Users.name:form.name,
        Users.last_name:form.last_name,
        Users.phone_number: form.phone_number,
        Users.password:form.password,
        Users.status:form.status,

    })
    db.commit()



def one_user(id,db):
    return db.query(Users).filter(Users.id==id).first()

def delete_users(id,db):
    db.query(Users).filter(Users.id==id).update({
        Users.status:False
    })

    db.commit()
    return {"data":"Malumot o'chirildi"}
