#!/usr/bin/env bash

function run_day() {
  if [ "$1" -lt "10" ]; then
    FILE="day0${1}.py"
  else
    FILE="day${1}.py"
  fi

  [ -f "${FILE}" ] && \
    printf "\n=== DAY ${1} ===\n" && \
    time uv run "${FILE}" ${2}
}

function run_all() {
  for i in {1..25}; do
    run_day "${i}"
  done
  printf "\n=============\n"
}

if [ "$#" -eq "0" ]; then
  time run_all
else
  run_day "${1}" "${2}"
fi

exit 0
