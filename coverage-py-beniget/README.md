# coverage.py + Beniget fixture

This combined fixture runs branch coverage and Beniget def-use analysis over the
same order-evaluation module. Its tests exercise both pricing branches, while
Beniget identifies the intentional `unused_note` definition.

Run with `bash run_coverage_beniget.sh` after installing the requirements.
