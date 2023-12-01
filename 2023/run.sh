#!/bin/bash

echo
echo Advent of Code 2023

for n in 01
do
    echo
    echo Day $n:
    time python3 day$n.py --no-submit
done

exit 0
