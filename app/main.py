from fastapi import FastAPI
from app.database import Base, engine
from app.routes import users, transactions, analytics

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Finance Tracker API")

@app.get("/")
def home():
    return {"message": "Finance Tracker API is running"}

app.include_router(users.router, prefix="/users", tags=["Users"])
app.include_router(transactions.router, prefix="/transactions", tags=["Transactions"])
app.include_router(analytics.router, prefix="/analytics", tags=["Analytics"])