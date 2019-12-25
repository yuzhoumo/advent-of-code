#!/usr/bin/env bash
printf "\nAdvent of Code 2019 Unit Tests\n\n"

for i in {1..9}
do
  printf "DAY $i: "
  if [ $i -lt 10 ]
  then
    python3 day0$i/day0$i\_test.py
  else
    python3 day$i/day$i\_test.py
  fi
  printf "\n"
done
