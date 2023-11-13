import datetime

from models.files import Files


def add_file(url,source,source_id,db):

    new_files = Files(
        file=url,
        source=source,
        source_id=source_id,
        date=datetime.datetime.today()
    )
    db.add(new_files)
    db.commit()
    db.refresh(new_files)
    return {"data": "Files add base"}