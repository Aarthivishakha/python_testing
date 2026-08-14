#!/usr/bin/env bash
set -u

ROOT="$(cd "$(dirname "$0")" && pwd)"
cd "$ROOT"

bandit -r sast_fixture.py -f json
bandit_status=$?
semgrep --config auto sast_fixture.py --json
semgrep_status=$?

if [[ $bandit_status -gt 1 || $semgrep_status -gt 1 ]]; then
    exit 2
fi

if [[ $bandit_status -eq 1 || $semgrep_status -eq 1 ]]; then
    exit 1
fi
