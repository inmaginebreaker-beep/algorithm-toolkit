import logging

from algorithm_toolkit.config import APP_NAME, DEBUG
from algorithm_toolkit.logging_config import setup_logging

logger = logging.getLogger(__name__)


def main():

    setup_logging()

    logger.info(f"{APP_NAME} started")

    logger.info(f"debug={DEBUG}")


if __name__ == "__main__":
    main()
