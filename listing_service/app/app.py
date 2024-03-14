from fastapi import FastAPI
import logging


logger = logging.getLogger(__name__)

app = FastAPI()


@app.get("/home")
def read_root():
    logger.info("request recieved")
    return {"Hello": "World"}
