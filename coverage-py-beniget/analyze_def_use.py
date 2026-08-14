"""Report dead definitions in the combined fixture using Beniget."""

import json
from pathlib import Path

import gast as ast
from beniget import DefUseChains


TARGET = Path(__file__).resolve().parent / "combined_analysis.py"


def main():
    module = ast.parse(TARGET.read_text(encoding="utf-8"))
    chains = DefUseChains(filename=TARGET.name)
    chains.visit(module)
    dead_definitions = []
    for chain in chains.chains.values():
        if not chain.users():
            name = getattr(chain.node, "id", None) or getattr(
                chain.node, "name", None
            )
            if name:
                dead_definitions.append(name)
    print(
        json.dumps(
            {
                "total_def_use_chains": len(chains.chains),
                "dead_defs": sorted(set(dead_definitions)),
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
