import sys

""" Day 1: The Tyranny of the Rocket Equation (Part 2)

Fuel itself requires fuel just like a module - take its mass, divide by three, round down, and subtract 2. However, that
fuel also requires fuel, and that fuel requires fuel, and so on. Any mass that would require negative fuel should
instead be treated as if it requires zero fuel. What is the sum of the fuel requirements for all of the modules on your
spacecraft when also taking into account the mass of the added fuel? (Calculate the fuel requirements for each module
separately, then add them all up at the end.) """


def calc_fuel(mass):
    fuel = mass // 3 - 2
    if fuel <= 0:
        return 0
    return fuel + calc_fuel(fuel)


def main():
    assert len(sys.argv) > 1, 'Missing argument: path to input file'
    assert len(sys.argv) < 3, 'Too many arguments'
    input_file = sys.argv[1]

    with open(input_file, 'r') as f:
        print(sum(calc_fuel(int(mass)) for mass in f.readlines()))


if __name__ == '__main__':
    main()
