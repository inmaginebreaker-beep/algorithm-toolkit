import logging

from algorithm_toolkit.application.algorithm_service import AlgorithmService
from algorithm_toolkit.cli.commands import create_parser, run_command
from algorithm_toolkit.exceptions import AlgorithmToolkitError
from algorithm_toolkit.logging_config import setup_logging

logger = logging.getLogger(__name__)


def main() -> int:
    setup_logging()

    parser = create_parser()
    args = parser.parse_args()

    service = AlgorithmService()

    try:
        return run_command(
            args,
            service,
        )

    except AlgorithmToolkitError as error:
        logger.error("%s", error)
        return 1

    except Exception:
        logger.exception("Unexpected error")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
