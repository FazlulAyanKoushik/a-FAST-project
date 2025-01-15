# A simple FastAPI project with JWT authentication
A simple FastAPI project for practice.


## Installation
```bash
pip install -r requirements.txt
```

## Database Migrations
```bash
python -m app.migrations.migrate_users
```

## Run
```bash
uvicorn app.main:app --reload
```

## Command for remove __pycache__
```bash
find . | grep -E "(__pycache__|\.pyc|\.pyo$)" | xargs rm -rf
```

```angular2html
find . -name "__pycache__" -exec rm -r {} +
```