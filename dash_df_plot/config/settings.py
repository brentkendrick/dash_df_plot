"""
If not running Docker then explicitely load dot_env since we want to run the app with options other than "FLASK RUN"
(which loads .env) by default.  In the Docker setup this isn't needed since we load the .env through the docker-compose cmds.
"""

import os
from pathlib import Path

from dotenv import load_dotenv

# Enable use of .env variables
load_dotenv()

# returns the directory where this file resides
dir_name = Path(__file__).resolve().parent

# Establish path to the dashapps/assets folder
# so that assets specific to the dash apps can be served
ASSETS_PATH = str(dir_name.parent / "assets")
# Location of static files with help documentation
DOCUMENTATION_PATH = dir_name.parent / "doc"
# Redis.
REDIS_URL = os.getenv("REDIS_URL", "redis://redis:6379/0")
REDIS_HOST = os.getenv("REDIS_HOST", "redis")

FPTRACE_BASE_URI = os.getenv("FPTRACE_BASE_URI", "/")
FPTRACE_PORT = os.getenv("FPTRACE_PORT", "5000")
SERVER_NAME = os.getenv(
    "SERVER_NAME", "localhost:{0}".format(os.getenv("PORT", "8000"))
)
