import logging

from algorithm_toolkit.algorithms.array import two_sum
from algorithm_toolkit.logging_config import setup_logging

logger = logging.getLogger(__name__)
def main() -> None:
    setup_logging()

    logger.info(
        "Algorithm Toolkit started"
    )


if __name__ == "__main__":
    main()
