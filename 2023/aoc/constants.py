import pathlib

YEAR = 2023
URL = f"https://adventofcode.com/{YEAR}/day/{{day}}"

THIS_DIR = pathlib.Path(__file__).parent
SOLUTION_DIR = THIS_DIR.parent
TEMPLATE_FILE = THIS_DIR / "template.txt"
INPUTS_FILE = THIS_DIR / "inputs.json"
SUBMISSIONS_FILE = THIS_DIR / "submissions.json"

TOKEN_FILE = THIS_DIR / ".token"
