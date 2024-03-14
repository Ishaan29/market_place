import logging
from logging.handlers import RotatingFileHandler
import os

# Define the base directory where log files will be stored
LOG_DIR = "logs"
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

# Basic configuration for logging
LOGGING_CONFIG = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'default': {
            'format': '%(levelname)s - %(message)s',
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'default',
            'stream': 'ext://sys.stdout',  # Use sys.stdout instead of the default sys.stderr
        },
        'file': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'default',
            'filename': os.path.join(LOG_DIR, 'app.log'),
            'maxBytes': 10485760,  # 10MB
            'backupCount': 5,      # Keep at most 5 log files
            'encoding': 'utf8',
        },
    },
    'loggers': {
        '': {  # root logger
            'handlers': ['console', 'file'],
            'level': 'INFO',
            'propagate': True,
        },
        'uvicorn': {
            'handlers': ['console', 'file'],
            'level': 'INFO',
            'propagate': False,
        },
        'uvicorn.error': {
            'handlers': ['console', 'file'],
            'level': 'INFO',
            'propagate': False,
        },
        'fastapi': {
            'handlers': ['console', 'file'],
            'level': 'INFO',
            'propagate': False,
        },
    },
}

# Function to configure logging
def configure_logging():
    logging.config.dictConfig(LOGGING_CONFIG)

# Then, call configure_logging() early in your main application file before creating the FastAPI app instance.
