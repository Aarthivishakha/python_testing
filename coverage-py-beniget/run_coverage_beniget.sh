#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "$0")" && pwd)"
cd "$ROOT"

pytest --cov=combined_analysis --cov-branch --cov-report=term-missing test_combined_analysis.py
python analyze_def_use.py
