# Finance Tracker Backend

## About the Project
This project is a simple finance tracking backend built using FastAPI.  
It allows users to store and manage their income and expenses and also view basic financial summaries.

The goal of this project was to design a clean and structured backend system that handles data properly and follows good coding practices.

---

## Features
- User registration and login
- Role-based access (Admin, Analyst, Viewer)
- Create, update, delete financial transactions
- Filter transactions by type and category
- Search transactions
- Pagination support
- Financial summary (total income, total expense, balance)
- Category-wise breakdown

---

## Tech Stack
- Python
- FastAPI
- SQLite
- SQLAlchemy

---

## Project Structure
The project is organized into different layers:

- `models.py` → database structure  
- `schemas.py` → request/response validation  
- `crud.py` → business logic  
- `routes/` → API endpoints  
- `main.py` → application entry point  

---

## How to Run the Project

1. Install dependencies:
2. pip install -r requirements.txt
3. 2. Run the server:
   3. http://127.0.0.1:8000/docs
   4. ---

## How to Test
- First create a user  
- Then login to get a token  
- Use that user to create transactions  
- Check analytics endpoints  

---

## Assumptions
- Authentication is implemented in a simple way using JWT  
- Roles are basic and used only for access control  
- SQLite is used for simplicity  

---

## What I Focused On
- Keeping the code clean and readable  
- Separating logic properly (routes, models, etc.)  
- Making sure APIs work correctly  
- Handling errors and validation  

---

## Future Improvements
- Add frontend dashboard  
- Improve authentication (refresh tokens, etc.)  
- Add monthly and yearly reports  
- Deploy with a proper database  

---

## Author
Rohith Reddy
