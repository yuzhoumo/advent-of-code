# Advent of Code 2024

My Python solutions for Advent of Code 2024

## Prerequisites

- `uv` Python package manager
- `make` Build utility

After installing the dependencies, log in to the advent of code website and
get your session token from the browser cookies. Paste this token into a file
nameds `aoc/.token`.

## Usage

Source the environment file for a particular day and test file:
```
. ./scripts/env.sh 1 test/1.txt
```

This script will set up aliases and source the Python virtual env:
```
s -> run full day 1 input and submit
i -> run full day 1 input (or provide optional path to input file)
t -> run test day 1 input from file: test/1.txt
uv sync
Resolved 9 packages in 0.45ms
Audited 8 packages in 0.01ms
```

To set up a template file for a particular day, run:
```
make template day=1
```
