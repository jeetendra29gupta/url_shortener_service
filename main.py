import logging
from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI

from database import initialize_database, create_indexes
from routers import url_shortening, metrics

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Starting lifespan...")
    initialize_database()
    create_indexes()
    yield
    logger.info("Shutting down...")


app = FastAPI(lifespan=lifespan)

app.include_router(url_shortening.router)
app.include_router(metrics.router)


@app.get("/")
def index_endpoint():
    return {"message": "Hello, World!"}


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8181)
