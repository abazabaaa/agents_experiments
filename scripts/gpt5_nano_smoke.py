"""Smoke test runner that processes artifacts/lark_docs.json with GPT-5-nano."""

from __future__ import annotations

import argparse
import shutil
import time
from pathlib import Path

import sys


ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if SRC.exists() and str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from agent_pipeline.config import load_config
from agent_pipeline.pipeline import run_pipeline


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run GPT-5-nano smoke test for the agent pipeline.")
    parser.add_argument(
        "--config",
        default="configs/smoke_gpt5_nano.json",
        help="Path to smoke-test configuration JSON.",
    )
    parser.add_argument(
        "--clean",
        action="store_true",
        help="Remove the output directory before running the smoke test.",
    )
    parser.add_argument(
        "--quiet",
        action="store_true",
        help="Reduce console logging during pipeline execution.",
    )
    parser.add_argument(
        "--expect",
        type=int,
        default=97,
        help="Expected number of output documents (default: 97).",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    config = load_config(args.config)
    output_dir = config.output_directory

    if args.clean and output_dir.exists():
        shutil.rmtree(output_dir)

    start = time.perf_counter()
    run_pipeline(config, quiet=args.quiet)
    duration = time.perf_counter() - start

    if not output_dir.exists():
        raise SystemExit(f"Smoke test failed: output directory {output_dir} was not created")

    produced_files = [p for p in output_dir.iterdir() if p.is_file()]
    count = len(produced_files)
    print(f"Smoke test completed in {duration:.1f}s. Produced {count} documents in {output_dir}.")

    if count < args.expect:
        raise SystemExit(
            f"Smoke test failed: expected at least {args.expect} documents but found {count}"
        )

    return 0


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())
