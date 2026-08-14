# Semgrep + Bandit fixture

This SAST fixture intentionally includes a hardcoded password, MD5 password
hashing, and SQL query concatenation so both Bandit and Semgrep produce security
findings.

Run with `bash run_sast.sh` after installing both scanners.
