from collections import namedtuple
from typing import List

import math
import sys

""" Day 10: Monitoring Station (Part 1)
Your job is to figure out which asteroid would be the best place to
build a new monitoring station. A monitoring station can detect any
asteroid to which it has direct line of sight - that is, there cannot
be another asteroid exactly between them. This line of sight can be at
any angle, not just lines aligned to the grid or diagonally. The best
location is the asteroid that can detect the largest number of other
asteroids. Find the best location for a new monitoring station. How many
other asteroids can be detected from that location?
"""

Point = namedtuple('Asteroid', 'x y')

def parse(raw: str) -> List[Point]:
    return [
        Point(x, y)
        for y, row in enumerate(raw.strip().splitlines())
        for x, c in enumerate(row)
        if c == '#'
    ]


def most_visible(asteroids: List[Point]) -> int:
    most = -float('inf')
    for asteroid in asteroids:
        count = count_visible(asteroid, asteroids)
        if count > most:
            most = count

    return most


def count_visible(station: Point, asteroids: List[Point]) -> int:
    slopes = set()
    for asteroid in asteroids:
        dx = station.x - asteroid.x
        dy = station.y - asteroid.y
        gcd = math.gcd(dx, dy)

        if not (dx == dy == 0):
            slope = (dy // gcd, dx // gcd)
            slopes.add(slope)

    return len(slopes)


def main():
    assert len(sys.argv) > 1, 'Missing argument: path to input file'
    input_file = sys.argv[1]

    with open(input_file, 'r') as f:
        asteroids = parse(f.read())

    print(most_visible(asteroids))


if __name__ == '__main__':
    main()
