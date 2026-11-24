# Read-only. Run: rye run python examples/routine_files.py EXECUTION_ID OUTPUT_PATH
import sys
from pathlib import Path

from mobilerun_sdk import MobilerunSDK


def routine_files(sdk: MobilerunSDK, execution_id: str, output: Path) -> bytes:
    sdk.routine_files.list_folders()
    for file in sdk.routine_files.list(execution_id=execution_id):
        content = file.download()
        output.write_bytes(content)
        return content
    raise RuntimeError("No saved routine file fixture for this execution")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        raise SystemExit("Pass execution ID and output path")
    routine_files(MobilerunSDK(), sys.argv[1], Path(sys.argv[2]))
