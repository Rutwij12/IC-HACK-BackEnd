cd src

# TEST_ENV="TEST"
TEST_ENV="PROD"

echo "starting server"
poetry run fastapi run main.py | tee -a server.log &

SERVER=$!

echo "starting celery worker"
poetry run celery -A worker worker --loglevel=info | tee -a worker.log &

CELERY=$!

wait $SERVER
wait $CELERY