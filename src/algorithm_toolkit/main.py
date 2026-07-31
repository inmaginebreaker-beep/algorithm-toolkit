import logging

from algorithm_toolkit.cli.commands import (
    create_parser,
    run_command,
)
from algorithm_toolkit.logging_config import setup_logging

logger = logging.getLogger(__name__)


def main() -> int:
    setup_logging()

    parser = create_parser()

    args = parser.parse_args()

    try:
        return run_command(args)

    except Exception:
        logger.exception("CLI execution failed")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
