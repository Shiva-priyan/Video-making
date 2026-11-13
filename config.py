"""Load settings from a .env file into environment variables.

Usage from other modules:

    from config import settings
    api_key = settings["VIDEO_API_KEY"]
"""

import os

from dotenv import load_dotenv

# Reads .env from the project root and copies each KEY=value line into
# os.environ. Variables already set in the shell are NOT overwritten.
load_dotenv()


def require(name: str) -> str:
    """Return an environment variable, or fail loudly if it is missing."""
    value = os.getenv(name)
    if not value:
        raise RuntimeError(f"Missing {name}. Add it to your .env file.")
    return value


settings = {
    "VIDEO_API_KEY": os.getenv("VIDEO_API_KEY", ""),
    "OUTPUT_DIR": os.getenv("OUTPUT_DIR", "output"),
}
