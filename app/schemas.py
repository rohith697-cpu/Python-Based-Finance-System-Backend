from pydantic import BaseModel
from datetime import date

# ---------- USER ----------
class UserCreate(BaseModel):
    name: str
    role: str
    password: str


class UserResponse(BaseModel):
    id: int
    name: str
    role: str

    class Config:
        from_attributes = True


# ---------- TRANSACTION ----------
class TransactionCreate(BaseModel):
    amount: float
    type: str
    category: str
    date: date
    notes: str | None = None
    user_id: int


class TransactionResponse(BaseModel):
    id: int
    amount: float
    type: str
    category: str
    date: date
    notes: str | None = None
    user_id: int

    class Config:
        from_attributes = True