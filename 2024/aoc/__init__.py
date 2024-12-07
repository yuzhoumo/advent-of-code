from typing import Callable
import argparse
import bs4
import json
import pathlib
import re
import requests
import string
import sys
import time
import webbrowser
from .constants import *


__all__ = ("make_template", "day", "submit", "run")


def make_template(): # setup template for a given day
    assert len(sys.argv) == 2

    day = sys.argv[1]
    assert all(d.isdigit for d in day), "day must be an integer"

    day = int(day)
    assert 1 <= day <= 25, "day must be between 1-25"

    sol_file = SOL_DIR / (f"day0{day}.py" if day < 10 else f"day{day}.py")
    if not sol_file.exists():
        t = string.Template(TEMPLATE_FILE.read_text())
        sol_file.write_text(t.safe_substitute(day=day))
        print(f"template created: {sol_file}")
    else:
        print(f"file already exists: {sol_file}")


def day(d: int):
    if not INPUTS_FILE.exists(): INPUTS_FILE.write_text("{}")
    key, inputs = str(d), json.loads(INPUTS_FILE.read_text())
    if key in inputs: return inputs[key]

    response = requests.get(url=URL.format(day=d) + "/input", cookies=COOKIES)
    if not response.ok: raise ValueError("error: request failed")

    inputs[key] = response.text.strip()
    INPUTS_FILE.write_text(json.dumps(inputs, indent=2))
    return inputs[key]


def _pretty_print(message):

    fmt = {
        'g': '\x1b[32m',
        'y': '\x1b[33m',
        'r': '\x1b[31m',
        'rst': '\x1b[0m',
        'bld': '\x1b[1m',
    }

    match message[7]:
        case "t":
            # "That's the right answer! ..."
            color = fmt['g']
        case "'" | "e":
            # "You don't seem to be solving the right level. ..."
            # "You gave an answer too recently; you have to wait ..."
            color = fmt['y']
        case "n":
            # "That's not the right answer. If you're stuck, ..."
            color = fmt['r']
        case _:
            raise ValueError("Unexpected message.", message)

    print(f"{fmt['bld']}{color}{message}{fmt['rst']}")


def submit(day, sol, part):
    if not (1 <= part <= 2):
        raise ValueError("Solution part must be 1 or 2")
    part = str(part)

    response = requests.post(
        url=URL.format(day=day) + "/answer",
        cookies=COOKIES,
        data={"level": part, "answer": sol},
        timeout=10,
    )

    if not response.ok:
        raise ValueError("request failed")

    soup = bs4.BeautifulSoup(response.text, "html.parser")
    article = soup.find('article')
    if not article:
        raise ValueError("Could not parse response HTML")

    message = article.text
    if "You gave an answer too recently" in message:
        match = re.search(r"(?:(\d+)m )?(\d+)s", message)
        if not match:
            raise ValueError("Could not parse wait time")

        minutes, seconds = match.groups()
        wait_time = 60 * int(minutes or 0) + int(seconds)

        while wait_time > 0:
            print(f"Waiting {wait_time} seconds to retry...")
            time.sleep(1)
            wait_time -= 1

    if "That's the right answer" in message:
        if part == 1: webbrowser.open(response.url) # view part 2

    _pretty_print(message)


def run(solve: Callable, d: int):
    parser = argparse.ArgumentParser()
    parser.add_argument('input_file', nargs='?', type=pathlib.Path)
    parser.add_argument('--submit', action='store_true')
    args = parser.parse_args()

    sol1, sol2 = None, None
    if args.input_file:
        sol1, sol2 = solve(args.input_file.read_text())
    else:
        sol1, sol2 = solve(day(d))

    print(f"part1: {sol1}\npart2: {sol2}")

    if args.submit:
        if sol1 is not None:
            print("\nsubmitting part 1...")
            submit(d, sol1, 1)
        if sol2 is not None:
            print("\nsubmitting part 2...")
            submit(d, sol2, 2)

    return sol1, sol2

