import sys
import re

# Part 1
def is_valid_count(line):
    p = re.compile('[-: ]+')
    lo, hi, c, password = p.split(line)
    cnt = password.count(c)
    return cnt >= int(lo) and cnt <= int(hi)


# Part 2
def is_valid_index(line):
    p = re.compile('[-: ]+')
    i, j, c, password = p.split(line)
    i, j = int(i) - 1, int(j) - 1
    return (password[i] == c) != (password[j] == c)


def main():
    assert len(sys.argv) > 1, 'Missing argument: path to input file'
    assert len(sys.argv) < 3, 'Too many arguments'
    input_file = sys.argv[1]

    with open(input_file, 'r') as f:
        text = f.read().strip()
        lines = text.splitlines()

    # Counter function
    num_valid = lambda lines, func: sum(1 for x in lines if func(x))

    print('\nInput:\n{0}'.format(text))
    print('\nPart 1:', num_valid(lines, is_valid_count))
    print('\nPart 2:', num_valid(lines, is_valid_index))


if __name__ == '__main__':
    main()
