#!/usr/bin/env bash

# must be sourced: source ./scripts/aliases.sh <day> <test_input_file>

DAY=$(printf "%02d" "$1")
INPUT="test/${1}.txt"

echo "s -> run full day ${1} input and submit"
alias s="uv run day${DAY}.py --submit"

echo "i -> run full day ${1} input (or provide optional path to input file)"
alias i="uv run day${DAY}.py"

echo "t -> run test day ${1} input from file: ${INPUT}"
alias t="uv run day${DAY}.py ${INPUT}"
