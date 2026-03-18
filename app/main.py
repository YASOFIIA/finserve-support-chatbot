from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from dotenv import load_dotenv
from app.routers.chat import router
from pathlib import Path
load_dotenv()

BASE_DIR = Path(__file__).parent.parent
app = FastAPI()
app.include_router(router)
app.mount("/static", StaticFiles(directory=BASE_DIR / "static"), name="static")

@app.get("/")
def index():
    return FileResponse(BASE_DIR / "static" / "index.html")