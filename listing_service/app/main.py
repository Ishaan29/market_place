import os
from dotenv import load_dotenv
import uvicorn
import logging

from log import configure_logging
logger = logging.getLogger(__name__)


configure_logging()

if __name__ == "__main__":
    load_dotenv()
    port = int(os.getenv('PORT'))
    host = os.getenv('HOST')
    logger.info(f"Starting listing service at port: {port}")
    try:
        uvicorn.run("app:app", host=host, port=port, reload=True)
    except Exception:
        logger.error("Error while starting up the service")
        raise RuntimeError("Error while starting the service")