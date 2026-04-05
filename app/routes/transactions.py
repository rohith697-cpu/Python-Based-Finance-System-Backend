from fastapi import APIRouter, Depends, HTTPException, Header
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app import schemas, crud

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def check_admin(user):
    if user.role != "admin":
        raise HTTPException(status_code=403, detail="Admin access required")


@router.post("/")
def create_transaction(
    txn: schemas.TransactionCreate,
    user_id: int = Header(...),
    db: Session = Depends(get_db)
):
    user = crud.get_user_by_id(db, user_id)

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    check_admin(user)

    return crud.create_transaction(db, txn)


@router.get("/")
def read_transactions(
    skip: int = 0,
    limit: int = 10,
    db: Session = Depends(get_db)
):
    return crud.get_transactions(db, skip, limit)


@router.put("/{id}")
def update_transaction(
    id: int,
    txn: schemas.TransactionCreate,
    user_id: int = Header(...),
    db: Session = Depends(get_db)
):
    user = crud.get_user_by_id(db, user_id)

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    check_admin(user)

    updated = crud.update_transaction(db, id, txn)

    if not updated:
        raise HTTPException(status_code=404, detail="Transaction not found")

    return updated


@router.delete("/{id}")
def delete_transaction(
    id: int,
    user_id: int = Header(...),
    db: Session = Depends(get_db)
):
    user = crud.get_user_by_id(db, user_id)

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    check_admin(user)

    deleted = crud.delete_transaction(db, id)

    if not deleted:
        raise HTTPException(status_code=404, detail="Transaction not found")

    return {"message": "Deleted successfully"}