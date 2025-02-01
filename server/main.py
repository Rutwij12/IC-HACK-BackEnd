from fastapi import FastAPI
from fastapi.responses import PlainTextResponse

app = FastAPI()

@app.get("/")
def read_root():
    return PlainTextResponse("OK")