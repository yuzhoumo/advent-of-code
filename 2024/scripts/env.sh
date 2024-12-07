#!/usr/bin/env bash

# must be sourced: source ./scripts/env.sh <day> <test_input_file>

echo "s -> run full day ${1} input and submit"
alias s="make submit day=${1}"

echo "i -> run full day ${1} input (or provide optional path to input file)"
alias i="make run day=${1}"

echo "t -> run test day ${1} input from file: ${2}"
alias t="make run day=${1} input=${2}"

make install
. ./.venv/bin/activate
