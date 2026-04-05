from sqlalchemy.orm import Session
from app import models

# ---------- USERS ----------
def create_user(db: Session, user):
    new_user = models.User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def get_user_by_name(db: Session, name: str):
    return db.query(models.User).filter(models.User.name == name).first()


def get_user_by_id(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


# ---------- TRANSACTIONS ----------
def create_transaction(db: Session, txn):
    new_txn = models.Transaction(**txn.dict())
    db.add(new_txn)
    db.commit()
    db.refresh(new_txn)
    return new_txn


def get_transactions(db: Session, skip=0, limit=10):
    return db.query(models.Transaction).offset(skip).limit(limit).all()


def update_transaction(db: Session, txn_id: int, updated_data):
    txn = db.query(models.Transaction).filter(models.Transaction.id == txn_id).first()

    if not txn:
        return None

    for key, value in updated_data.dict().items():
        setattr(txn, key, value)

    db.commit()
    db.refresh(txn)
    return txn


def delete_transaction(db: Session, txn_id: int):
    txn = db.query(models.Transaction).filter(models.Transaction.id == txn_id).first()

    if txn:
        db.delete(txn)
        db.commit()

    return txn