#!/bin/bash

echo
echo Advent of Code 2020

for n in 01 02 03 04 05 06 07 08 09 10 11 12 13 14 15 16 17 18
do
    echo
    echo Day $n:
    time python3 day$n/day$n.py day$n/input.txt
done

exit 0