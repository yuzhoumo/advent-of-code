import sys


def main():
    assert len(sys.argv) > 1, 'Missing argument: path to input file'
    assert len(sys.argv) < 3, 'Too many arguments'

    with open(sys.argv[1], 'r') as f:
        print('WORK_IN_PROGRESS')


if __name__ == '__main__':
    main()
