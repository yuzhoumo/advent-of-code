import pathlib

YEAR          = 2024
URL           = f"https://adventofcode.com/{YEAR}/day/{{day}}"
THIS_DIR      = pathlib.Path(__file__).parent
SOL_DIR       = THIS_DIR.parent
INPUTS_FILE   = THIS_DIR / "inputs.json"
TEMPLATE_FILE = THIS_DIR / "template.txt"
TOKEN_FILE    = THIS_DIR / ".token"
COOKIES       = {"session": TOKEN_FILE.read_text().strip()}
