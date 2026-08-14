"""Mine this repository's Git history and report per-file code churn.

Usage:
    python run_pydriller.py
"""

import json
from collections import defaultdict
from pathlib import Path

from pydriller import Repository


REPOSITORY_ROOT = Path(__file__).resolve().parent.parent


def main(max_commits=200):
    """Analyze reachable commits and print a JSON churn summary."""
    churn = defaultdict(lambda: {"commits": 0, "added": 0, "removed": 0})
    commits_seen = 0

    for commit in Repository(str(REPOSITORY_ROOT)).traverse_commits():
        commits_seen += 1
        for modified_file in commit.modified_files:
            path = modified_file.new_path or modified_file.old_path
            if not path:
                continue

            path = path.replace("\\", "/")
            churn[path]["commits"] += 1
            churn[path]["added"] += modified_file.added_lines
            churn[path]["removed"] += modified_file.deleted_lines

        if commits_seen >= max_commits:
            break

    top_churned = sorted(
        churn.items(), key=lambda item: item[1]["commits"], reverse=True
    )[:10]
    summary = {
        "commits_analyzed": commits_seen,
        "files_touched": len(churn),
        "top_churned_files": [
            {"path": path, **statistics} for path, statistics in top_churned
        ],
    }
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
