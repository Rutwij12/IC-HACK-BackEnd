from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
from routes.video_gen import router as video_router

app = FastAPI()

app.include_router(video_router)

@app.get("/")
def read_root():
    return PlainTextResponse("OK")