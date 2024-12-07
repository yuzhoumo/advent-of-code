#!/usr/bin/env bash

run_day() {
    local file

    # format day number with leading zero
    printf -v file "day%02d.py" "$1"

    if [[ -f "$file" ]]; then
        printf "\n=== DAY %d ===\n" "$1"
        time uv run "$file" "$2" "$3"
    fi
}

run_all() {
    local day
    for day in {1..25}; do
        run_day "$day"
    done
    printf "\n=============\n"
}

main() {
    if [[ $# -eq 0 ]]; then
        time run_all
    else
        run_day "$1" "$2" "$3"
    fi
}

main "$@"
exit 0
