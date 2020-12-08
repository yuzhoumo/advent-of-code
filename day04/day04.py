import sys
import re

# Part 1
def is_valid_weak(passport):
    """
    Perform a weak check given a string representing the contents
    of a passport. Returns true if all required fields are present,
    False otherwise.
    """

    # Names of required fields
    required = ('byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid')

    # Split the passport fields
    p = re.compile('[:\n ]')
    tokens = set(p.split(passport))

    for r in required:
        if r not in tokens:
            return False

    return True


# Part 2
def is_valid_strong(passport):
    """
    Perform a strong check given a string representing the contents
    of a passport. Returns true if all required fields are present and
    content of each field is valid, False otherwise.
    """

    # Used to ensure that each field appears exactly once
    counts = [0, 0, 0, 0, 0, 0, 0]

    # Split the password fields
    p = re.compile('[:\n ]')
    tokens = p.split(passport)

    for i in range(0, len(tokens), 2):

        key = tokens[i]
        val = tokens[i+1]

        if key == 'byr':
            counts[0] += 1
            year = int(val) if re.match('^[1-9][0-9]{3}$', val) else -1
            if year < 1920 or year > 2002:
                return False

        elif key == 'iyr':
            counts[1] += 1
            year = int(val) if re.match('^[1-9][0-9]{3}$', val) else -1
            if year < 2010 or year > 2020:
                return False

        elif key == 'eyr':
            counts[2] += 1
            year = int(val) if re.match('^[1-9][0-9]{3}$', val) else -1
            if year < 2020 or year > 2030:
                return False

        elif key == 'hgt':
            counts[3] += 1
            match = re.match('^([1-9][0-9]*)(cm|in)$', val)

            if not match:
                return False

            height, unit = match.groups()
            height = int(height)

            if unit == 'cm' and (height < 150 or height > 193):
                return False

            if unit == 'in' and (height < 59 or height > 76):
                return False

        elif key == 'hcl':
            counts[4] += 1
            if not re.match('^#[0-9abcdef]{6}$', val):
                return False

        elif key == 'ecl':
            counts[5] += 1
            if not re.match('^amb|blu|brn|gry|grn|hzl|oth$', val):
                return False

        elif key == 'pid':
            counts[6] += 1
            if not re.match('^[0-9]{9}$', val):
                return False

    return all(n == 1 for n in counts)


def main():
    assert len(sys.argv) > 1, 'Missing argument: path to input file'
    assert len(sys.argv) < 3, 'Too many arguments'
    input_file = sys.argv[1]

    with open(input_file, 'r') as f:
        text = f.read().strip()
        passports = text.split('\n\n')

    # Solve parts 1 and 2
    part1 = sum(1 for p in passports if is_valid_weak(p))
    part2 = sum(1 for p in passports if is_valid_strong(p))

    print('\nInput:\n{0}'.format(text))
    print('\nPart 1:', part1)
    print('\nPart 2:', part2)


if __name__ == '__main__':
    main()
