# main.py

from fastapi import FastAPI
from contextlib import asynccontextmanager
import uvicorn

from storage.database import create_tables
from api.v1.routes import auth, conversations


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_tables()   # creates SQLite tables on first run, no-op after
    yield


app = FastAPI(
    title="Docuflow",
    version="0.1.0",
    lifespan=lifespan,
)

app.include_router(auth.router, prefix="/api/v1")
app.include_router(conversations.router, prefix="/api/v1")


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)