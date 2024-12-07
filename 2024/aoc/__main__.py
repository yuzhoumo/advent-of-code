import sys
from string import Template
from .constants import *


def setup(): # setup template for a given day
    assert len(sys.argv) == 2

    day = sys.argv[1]
    assert all(d.isdigit for d in day), "day must be an integer"

    day = int(day)
    assert 1 <= day <= 25, "day must be between 1-25"

    sol_file = SOL_DIR / (f"day0{day}.py" if day < 10 else f"day{day}.py")
    if not sol_file.exists():
        t = Template(TEMPLATE_FILE.read_text())
        sol_file.write_text(t.safe_substitute(day=day))
        print(f"template created: {sol_file}")
    else:
        print(f"file already exists: {sol_file}")


setup()
