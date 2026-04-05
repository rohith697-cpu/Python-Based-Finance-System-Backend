from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey
from app.database import Base

# ---------- USER ----------
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    role = Column(String, nullable=False)
    password = Column(String, nullable=False)


# ---------- TRANSACTION ----------
class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)
    amount = Column(Float, nullable=False)
    type = Column(String, nullable=False)  # income / expense
    category = Column(String, nullable=False)
    date = Column(Date, nullable=False)
    notes = Column(String)
    user_id = Column(Integer, ForeignKey("users.id"))