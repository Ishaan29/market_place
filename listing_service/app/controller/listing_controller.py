from fastapi import APIRouter
import logging
logger = logging.getLogger(__name__)

router = APIRouter()

@router.get("/listing")
def getListing():
    logger.info("Recieved Listing call")
    return {"Hello": "World"}