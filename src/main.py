from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
from routes.video_gen import router as gen_video_router
from routes.video import router as video_router

app = FastAPI()

app.include_router(gen_video_router)
app.include_router(video_router, prefix="/videos")


@app.get("/")
def read_root():
    return PlainTextResponse("OK")
