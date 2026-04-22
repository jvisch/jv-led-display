from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[1]
SRC_PATH = PROJECT_ROOT / "src"

if str(SRC_PATH) not in sys.path:
    sys.path.insert(0, str(SRC_PATH))

# ----------------------------------------------

import sterrenhemel


def _run_effect():
    for entrypoint_name in ("starfield", "main"):
        entrypoint = getattr(sterrenhemel, entrypoint_name, None)
        if callable(entrypoint):
            entrypoint()
            return

    raise AttributeError(
        "Module 'sterrenhemel' must expose an explicit callable entrypoint "
        "such as 'starfield()' or 'main()' instead of relying on import side effects."
    )


_run_effect()
