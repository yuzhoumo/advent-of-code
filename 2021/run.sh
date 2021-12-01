#!/bin/bash

echo
echo Advent of Code 2020

for n in 01
do
    echo
    echo Day $n:
    time python3 day$n/day$n.py day$n/input.txt
done

exit 0