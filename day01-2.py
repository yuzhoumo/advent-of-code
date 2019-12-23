import sys


def calc_fuel(mass):
    fuel = mass // 3 - 2
    if fuel <= 0:
        return 0
    return fuel + calc_fuel(fuel)


assert len(sys.argv) > 1, 'Missing argument: path to input file'
assert len(sys.argv) < 3, 'Too many arguments'

with open(sys.argv[1], 'r') as f:
    print(sum(calc_fuel(int(n)) for n in f.readlines()))
