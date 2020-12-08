import sys

# Part 1
def get_id(chars):
    n, tot = 1, 0
    for c in chars[::-1]:
        if c == 'B' or c == 'R':
            tot += n
        n *= 2

    return tot


# Part 2
def get_missing(ids):

    ids = sorted(ids)
    curr = ids[0]

    for n in ids:
        if curr != n:
            return curr
        curr += 1


def main():
    assert len(sys.argv) > 1, 'Missing argument: path to input file'
    assert len(sys.argv) < 3, 'Too many arguments'
    input_file = sys.argv[1]

    with open(input_file, 'r') as f:
        text = f.read().strip()
        seats = text.splitlines()

    # Get list of seat ids
    ids = [get_id(s) for s in seats]

    print('\nInput:\n{0}'.format(text))
    print('\nPart 1:', max(ids))
    print('\nPart 2:', get_missing(ids))


if __name__ == '__main__':
    main()
