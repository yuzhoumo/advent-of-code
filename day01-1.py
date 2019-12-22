import sys

assert len(sys.argv) > 1, 'Missing argument: path to input file'
assert len(sys.argv) < 3, 'Too many arguments'

with open(sys.argv[1], 'r') as f:
    print(sum(int(n) // 3 - 2 for n in f.readlines()))
