#!/usr/bin/env bash
printf "\nAdvent of Code 2019 Solutions\n\n"

for i in {1..9}; do printf "DAY $i PART 1: "

  if [ $i -eq 2 ]; then
    time python3 day02/day02_1.py inputs/day02.txt 12 2
    printf "\nDAY 2 PART 2: "
    time python3 day02/day02_2.py inputs/day02.txt 19690720

  elif [ $i -eq 4 ]; then
    time python3 day04/day04_1.py 353096 843212
    printf "\nDAY 4 PART 2: "
    time python3 day04/day04_2.py 353096 843212

  elif [ $i -eq 5 ]; then
    printf "\n\n"
    time python3 day05/day05_1.py inputs/day05.txt 1
    printf "\nDAY 5 PART 2:\n\n"
    time python3 day05/day05_2.py inputs/day05.txt 5

  elif [ $i -eq 8 ]; then
    time python3 day08/day08_1.py inputs/day08.txt 25 6
    printf "\nDAY 8 PART 2:\n\n"
    time python3 day08/day08_2.py inputs/day08.txt 25 6

  elif [ $i -eq 9 ]; then
    printf "\n\n"
    time python3 day09/day09_1.py inputs/day09.txt 1
    printf "\nDAY 9 PART 2:\n\n"
    time python3 day09/day09_1.py inputs/day09.txt 2

  else
    time python3 day0$i/day0$i\_1.py inputs/day0$i.txt
    printf "\nDAY $i PART 2: "
    time python3 day0$i/day0$i\_2.py inputs/day0$i.txt

  fi; printf "\n"; done
