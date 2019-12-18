def calc_fuel(mass):
    amt = mass//3-2
    if amt <= 0:
        return 0
    return amt + calc_fuel(amt)


def get_total(masses):
    tot = 0
    for m in masses:
        tot += calc_fuel(m)
    return tot


with open('input.txt', 'r') as f:
    masses = [int(m) for m in f.readlines()]
    print(get_total(masses))
