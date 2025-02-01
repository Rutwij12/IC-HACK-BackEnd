poetry run celery -A celery_worker.celery_app worker --loglevel=info
poetry run fastapi dev main.py
