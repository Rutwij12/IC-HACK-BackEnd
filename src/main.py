from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
from routes.video_gen import router as gen_video_router
from routes.video import router as video_router
from routes.vector import router as vector_router
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
load_dotenv()

app.include_router(gen_video_router)
app.include_router(video_router)
app.include_router(vector_router, prefix="/vector")


@app.get("/")
def read_root():
    return PlainTextResponse("OK")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
