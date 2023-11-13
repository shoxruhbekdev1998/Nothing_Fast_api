from fastapi import HTTPException
from sqlalchemy.orm import joinedload

from models.comments import Comments

from routes.auth import get_password_hash

from utils.pagination import pagination


def all_comments(search, id, from_date, end_date, page, limit, db, status):
    comments = db.query(Comments).options(joinedload(Comments.comment_files)).filter(Comments.id >= 0)
    if search:
         comments= comments.filter(Comments.name.like(search)|
                                   Comments.email.like(search)|
                                   Comments.phone_number.like(search))

    if id:
        comments = comments.filter(Comments.id == id)

    if from_date and end_date:
        comments = comments.filter(Comments.date >= from_date, Comments.date <= end_date)

    if status == True:
        comments = comments.filter(Comments.status == status)

    elif status == False:
        comments = comments.filter(Comments.status == status)

    else:
        comments = comments.filter(Comments.id >= 0)

    return pagination(form=comments, page=page, limit=limit)


def add_comments(name,last_name,comment,db):
    new_comments = Comments(
        name=name,
        last_name=last_name,
        comment=comment,

    )
    db.add(new_comments)
    db.commit()
    db.refresh(new_comments)

    return {"data": new_comments.id }


def update_comments(id, form, db):
    if one_comment(id=form.id, db=db) is None:
        raise HTTPException(status_code=400, detail="Bunday raqamli question yo'q")

    db.query(Comments).filter(Comments.id == id).update({
        Comments.name: form.name,
        Comments.last_name: form.email,
        Comments.comment: form.phone_number,
        Comments.status: form.status,

    })
    db.commit()


def one_comment(id, db):
    return db.query(Comments).filter(Comments.id == id).first()


def delete_comments(id, db):
    db.query(Comments).filter(Comments.id == id).update({
        Comments.status: False
    })

    db.commit()
    return {"data": "Malumot o'chirildi"}
