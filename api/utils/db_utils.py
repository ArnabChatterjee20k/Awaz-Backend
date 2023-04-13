from sqlalchemy.orm import Session
from ..models import User, Contacts


def add_to_db(db: Session, model: User.User | Contacts.Contacts | list[Contacts.Contacts]):
    def commit_to_db():
        db.commit()
        db.refresh(model)

    if isinstance(model, list):
        db.add_all(model)
    else:
        db.add(model)
    commit_to_db(db)
    return model


