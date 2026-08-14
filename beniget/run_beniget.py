"""Run Beniget DefUseChains and report unused definitions."""

import json
from pathlib import Path

import gast as ast
from beniget import DefUseChains


TARGET = Path(__file__).resolve().parent / "def_use_analysis.py"


def analyze_file(path):
    module = ast.parse(path.read_text(encoding="utf-8"))
    chains = DefUseChains(filename=path.name)
    chains.visit(module)

    dead_definitions = []
    for chain in chains.chains.values():
        if not chain.users():
            name = getattr(chain.node, "id", None) or getattr(
                chain.node, "name", None
            )
            if name:
                dead_definitions.append(name)
    return len(chains.chains), sorted(set(dead_definitions))


def main():
    chain_count, dead_definitions = analyze_file(TARGET)
    print(
        json.dumps(
            {
                "file": TARGET.name,
                "total_def_use_chains": chain_count,
                "dead_defs": dead_definitions,
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
