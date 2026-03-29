# Backend Template Implementation TODO

## Completed ✅
- [x] Create top-level files (pyproject.toml, README.md, .gitignore, .env.example, Dockerfile, docker-compose.yml, alembic.ini, .dockerignore)
- [x] Create src/backend_template/ core package: __init__.py, main.py, core/{config,security,logger}.py, db/{__init__,session}.py, redis/{__init__,client}.py
- [x] User functionality: models/user.py, schemas/user.py, crud/user.py, api/v1/api.py (full CRUD + login/JWT), mounted in main.py

## Pending ⏳
1. Initialize Alembic: docker-compose run app alembic init alembic
2. alembic revision --autogenerate -m "create user table" && alembic upgrade head
3. Create tests/: conftest.py, test_crud.py, test_api.py, pytest-asyncio
4. Lint: ruff check --fix, mypy src/
5. Run/test: venv install, uvicorn/pytest/docker-compose up
6. Optional: prometheus-fastapi-instrumentator for /metrics, celery for tasks

**Next step**: Tests + run commands/demo.



