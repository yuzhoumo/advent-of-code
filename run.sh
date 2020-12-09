#!/bin/bash

echo
echo Advent of Code 2020

for n in {1..9}
do
    echo
    echo Day $n:
    time python3 day0$n/day0$n.py day0$n/input.txt
done
exit 0