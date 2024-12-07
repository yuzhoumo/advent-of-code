from typing import Callable, Optional
import json
import pathlib
import requests
import sys
from .constants import *


__all__ = ("day", "run")


def day(d: int):
    if not INPUTS_FILE.exists(): INPUTS_FILE.write_text("{}")
    key, inputs = str(d), json.loads(INPUTS_FILE.read_text())
    if key in inputs: return inputs[key]

    response = requests.get(url=URL.format(day=d) + "/input", cookies=COOKIES)
    if not response.ok: raise ValueError("error: request failed")

    inputs[key] = response.text.strip()
    INPUTS_FILE.write_text(json.dumps(inputs, indent=2))
    return inputs[key]


def run(solve: Callable, d: int, p: Optional[int] = None):
    if len(sys.argv) > 1:
        return solve(pathlib.Path(sys.argv[1]).read_text())
    return solve(day(d), part=p)
