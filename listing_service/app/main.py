# main.py
import os
from dotenv import load_dotenv
import uvicorn
import logging
from fastapi import FastAPI

from log import configure_logging
from controller.listing_controller import router as listing_controller

app = FastAPI()

class FastAPIApp:
    def __init__(self, app_instance: FastAPI):
        self.app = app_instance
        self._configure_logging()
        self._load_dotenv()
        self._register_routers()

    def _configure_logging(self):
        configure_logging()

    def _load_dotenv(self):
        load_dotenv()

    def _register_routers(self):
        self.app.include_router(listing_controller)

if __name__ == "__main__":
    load_dotenv()
    FastAPIApp(app)
    port = int(os.getenv('PORT', 8000))
    host = os.getenv('HOST', '127.0.0.1')
    logger = logging.getLogger(__name__)
    logger.info(f"Starting the service at http://{host}:{port}")

    uvicorn.run("main:app", host=host, port=port, reload=True)
