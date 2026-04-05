from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models import Transaction

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/summary")
def get_summary(db: Session = Depends(get_db)):
    txns = db.query(Transaction).all()

    total_income = sum(t.amount for t in txns if t.type == "income")
    total_expense = sum(t.amount for t in txns if t.type == "expense")

    return {
        "total_income": total_income,
        "total_expense": total_expense,
        "balance": total_income - total_expense
    }


@router.get("/category")
def category_breakdown(db: Session = Depends(get_db)):
    txns = db.query(Transaction).all()

    result = {}

    for t in txns:
        if t.category not in result:
            result[t.category] = 0

        result[t.category] += t.amount

    return result