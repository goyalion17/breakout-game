import subprocess
import sys
from pathlib import Path

SYSTEM_SOUNDS = Path("/System/Library/Sounds")


def play(name):
    """Грає системний звук macOS (Pop, Tink, Basso, Glass, Sosumi). На інших системах нічого не робить."""
    path = SYSTEM_SOUNDS / f"{name}.aiff"
    if sys.platform != "darwin" or not path.exists():
        return
    subprocess.Popen(["afplay", str(path)], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
