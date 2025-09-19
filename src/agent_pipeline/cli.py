"""Command-line entry point for the agent pipeline."""

from __future__ import annotations

import argparse
from collections.abc import Sequence

from .config import load_config
from .pipeline import run_pipeline


def parse_args(argv: Sequence[str] | None = None) -> argparse.Namespace:
    """Parse command-line arguments."""

    parser = argparse.ArgumentParser(description="Run the agent document pipeline.")
    parser.add_argument(
        "--config",
        default="configs/agent_pipeline_optimized.json",
        help="Path to the pipeline configuration file.",
    )
    parser.add_argument(
        "--quiet",
        action="store_true",
        help="Reduce console logging output.",
    )
    return parser.parse_args(argv)


def main(argv: Sequence[str] | None = None) -> int:
    """CLI entry point compatible with ``python -m agent_pipeline.cli``."""

    args = parse_args(argv)
    config = load_config(args.config)
    run_pipeline(config, quiet=args.quiet)
    return 0


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())
