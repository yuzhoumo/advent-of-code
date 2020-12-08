import sys

# Part 1


# Part 2


def main():
    assert len(sys.argv) > 1, 'Missing argument: path to input file'
    assert len(sys.argv) < 3, 'Too many arguments'
    input_file = sys.argv[1]

    with open(input_file, 'r') as f:
        text = f.read().strip()

    print('\nInput:\n{0}'.format(text))
    print('\nPart 1:')
    print('\nPart 2:')


if __name__ == '__main__':
    main()
