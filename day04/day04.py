import sys
import re

# Part 1
def is_valid_weak(passport):
    """
    Perform a weak check given a string representing the contents of a passport.
    Returns true if all required fields are present, False otherwise.
    """

    # Names of required fields
    required = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}

    # Split the passport fields
    pattern = re.compile(r'([a-z]{3}):')
    fields = set(pattern.findall(passport))

    return all(req in fields for req in required)


# Part 2
def is_valid_strong(passport):
    """
    Perform a strong check given a string representing the contents of a
    passport. Returns true if all required fields are present and content of
    each field is valid, False otherwise.
    """

    patterns = { # Regex patterns for each field
        'byr': re.compile(r'^[1-9][0-9]{3}$'),
        'iyr': re.compile(r'^[1-9][0-9]{3}$'),
        'eyr': re.compile(r'^[1-9][0-9]{3}$'),
        'hgt': re.compile(r'^([1-9][0-9]*)(cm|in)$'),
        'hcl': re.compile(r'^#[0-9a-f]{6}$'),
        'ecl': re.compile(r'^amb|blu|brn|gry|grn|hzl|oth$'),
        'pid': re.compile(r'^[0-9]{9}$')
    }

    checks = { # Correctness checks for each field
        'byr': lambda x: int(x) < 1920 or int(x) > 2002,
        'iyr': lambda x: int(x) < 2010 or int(x) > 2020,
        'eyr': lambda x: int(x) < 2020 or int(x) > 2030,
        'hgt': lambda x: int(x[:-2]) < 59 or int(x[:-2]) > 76 if x[-2:] == 'in'\
                         else int(x[:-2]) < 150 or int(x[:-2]) > 193,
        'hcl': lambda x: False,
        'ecl': lambda x: False,
        'pid': lambda x: False
    }

    seen = set() # Used to ensure each required field appears exactly once

    # Split the passport fields
    pattern = re.compile(r'([a-z]{3}):([^\s]+)')
    pairs = pattern.findall(passport)

    # Check validity of each field
    for key, val in pairs:
        if key in patterns:
            invalid = key in seen \
               or not patterns[key].match(val) \
               or checks[key](val)

            if invalid: return False
            seen.add(key)

    # Check if every required field appears
    return len(seen) == len(checks)


def main():
    assert len(sys.argv) > 1, 'Missing argument: path to input file'
    assert len(sys.argv) < 3, 'Too many arguments'
    input_file = sys.argv[1]

    with open(input_file, 'r') as f:
        text = f.read().strip()
        passports = text.split('\n\n')

    # Solve part 1
    part1 = sum(1 for p in passports if is_valid_weak(p))
    print('\nPart 1:', part1)

    # Solve part 2
    part2 = sum(1 for p in passports if is_valid_strong(p))
    print('Part 2:', part2)


if __name__ == '__main__':
    main()
