# Simple Chat CRUD

Small starter app built with:

- React + Vite for the frontend
- FastAPI for the backend
- SQLite for the current database

The backend is intentionally simple. Database access lives in small CRUD helpers so moving to Supabase later should be easier than if everything was mixed directly into route handlers.

## Run the backend

```bash
cd backend
py -3.13 -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

The API runs at `http://127.0.0.1:8000`.

Python `3.13` is recommended here because the local machine also has `3.14`, and one dependency currently installs more smoothly on `3.13`.

## Run the frontend

```bash
cd frontend
npm install
npm run dev
```

The UI runs at `http://localhost:5173`.

## What it can do

- Create and delete users
- Create and delete conversations
- Send and delete messages
- List users, conversations, and messages

## Next step when moving to Supabase

Keep the frontend API calls the same and replace the backend persistence layer inside `backend/app/crud.py` and `backend/app/database.py`.
