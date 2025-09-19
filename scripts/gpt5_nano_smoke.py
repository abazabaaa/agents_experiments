"""Smoke test runner that processes artifacts/lark_docs.json with GPT-5-nano."""

from __future__ import annotations

import argparse
import shutil
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if SRC.exists() and str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from agent_pipeline.config import load_config  # noqa: E402
from agent_pipeline.pipeline import run_pipeline  # noqa: E402


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Run GPT-5-nano smoke test for the agent pipeline."
    )
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
    parser.add_argument(
        "--limit",
        type=int,
        default=None,
        help="Limit the number of documents to process (useful for testing).",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    config = load_config(args.config)
    output_dir = config.output_directory

    if args.clean and output_dir.exists():
        shutil.rmtree(output_dir)

    # Apply document limit if specified
    if args.limit:
        import json

        input_file = config.input_artifact
        with open(input_file) as f:
            data = json.load(f)

        # Limit the scraped_documents to the specified number
        if "scraped_documents" in data and len(data["scraped_documents"]) > args.limit:
            data["scraped_documents"] = data["scraped_documents"][: args.limit]
            # Write to a temporary file
            temp_file = input_file.parent / f"temp_limited_{input_file.name}"
            with open(temp_file, "w") as f:
                json.dump(data, f, indent=2)
            # Update config to use the limited file
            config.input_artifact = temp_file
            print(f"Limited processing to {args.limit} documents")

    start = time.perf_counter()
    run_pipeline(config, quiet=args.quiet)
    duration = time.perf_counter() - start

    # Clean up temp file if created
    if args.limit:
        temp_file = config.input_artifact
        if temp_file.name.startswith("temp_limited_"):
            temp_file.unlink()

    if not output_dir.exists():
        raise SystemExit(
            f"Smoke test failed: output directory {output_dir} was not created"
        )

    produced_files = [p for p in output_dir.iterdir() if p.is_file()]
    count = len(produced_files)
    print(
        f"Smoke test completed in {duration:.1f}s. Produced {count} documents in {output_dir}."
    )

    # Adjust expectation if limit was used
    expected = min(args.expect, args.limit) if args.limit else args.expect

    if count < expected:
        raise SystemExit(
            f"Smoke test failed: expected at least {expected} documents but found {count}"
        )

    return 0


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())
