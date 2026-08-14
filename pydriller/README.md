# PyDriller tool information

This fixture uses PyDriller 2.9 to mine this repository's real Git history and
produce a per-file code-churn report. It reports the number of commits analyzed,
files touched, and the ten files changed by the most commits.

PyDriller operates on Git history, so no separate source-code trigger fixture is
required.

Install and run:

```bash
python -m pip install "pydriller>=2.9"
cd pydriller
python run_pydriller.py
```
