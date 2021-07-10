import sys

""" Day 1: The Tyranny of the Rocket Equation (Part 1)

Fuel required to launch a given module is based on its mass.
Specifically, to find the fuel required for a module, take its mass,
divide by three, round down, and subtract 2. The Fuel Counter-Upper
needs to know the total fuel requirement. Individually calculate the
fuel needed for the mass of each module (your puzzle input), then add
together all the fuel values. What is the sum of the fuel requirements
for all of the modules on your spacecraft? """


def calc_fuel(mass: int) -> int:
    return mass // 3 - 2


def main():
    assert len(sys.argv) > 1, 'Missing argument: path to input file'
    assert len(sys.argv) < 3, 'Too many arguments'
    input_file = sys.argv[1]

    with open(input_file, 'r') as f:
        print(sum(calc_fuel(int(mass)) for mass in f.readlines()))


if __name__ == '__main__':
    main()
