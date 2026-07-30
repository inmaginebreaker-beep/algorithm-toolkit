import logging
from pathlib import Path

from algorithm_toolkit.config import LOG_LEVEL


def setup_logging() -> None:
    log_directory = Path("logs")
    log_directory.mkdir(exist_ok=True)

    logging.basicConfig(
        level=getattr(logging, LOG_LEVEL.upper(), logging.INFO),
        format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
        handlers=[
            logging.StreamHandler(),
            logging.FileHandler(
                log_directory / "app.log",
                encoding="utf-8",
            ),
        ],
        force=True,
    )