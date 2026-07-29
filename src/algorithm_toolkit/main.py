import logging

from algorithm_toolkit.application.algorithm_service import AlgorithmService
from algorithm_toolkit.config import APP_NAME, DEBUG
from algorithm_toolkit.exceptions import AlgorithmToolkitError
from algorithm_toolkit.logging_config import setup_logging

logger = logging.getLogger(__name__)


def main() -> int:
    setup_logging()

    logger.info("%s started", APP_NAME)
    logger.info("Debug mode: %s", DEBUG)

    service = AlgorithmService()

    try:
        two_sum_result = service.run_two_sum(
            nums=[2, 7, 11, 15],
            target=9,
        )
        logger.info("Application result: %s", two_sum_result)

        maximum = service.run_find_max([4, 9, 2, 7])
        logger.info("Maximum value: %s", maximum)

        reversed_nums = service.run_reverse_array([1, 2, 3, 4])
        logger.info("Reversed array: %s", reversed_nums)

    except AlgorithmToolkitError as error:
        logger.error("Application error: %s", error)
        return 1

    except Exception:
        logger.exception("Unexpected application error")
        return 1

    logger.info("%s finished successfully", APP_NAME)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
