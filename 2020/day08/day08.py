import sys

# Part 1
def detect_loop(instructions):
    """
    Take an array of `instructions` of the form:
    
        [('acc', 5), ('nop', 0), ('jmp', -2), ...]

    Return True, `accumulator` right before the first time the same instruction
    is run more than once. Otherwise, return False, `accumulator` if no loop
    is detected.
    """

    ptr, accumulator, seen = 0, 0, set()
    while ptr < len(instructions):

        if ptr in seen:
            return True, accumulator

        seen.add(ptr)
        i, n = instructions[ptr]

        if i == 'acc':
            accumulator += n
            ptr += 1
        elif i == 'jmp':
            ptr += n
        elif i == 'nop':
            ptr += 1

    return False, accumulator


# Part 2
def fix_program(instructions):
    """
    Swap each nop/jmp instruction and check if the new program loops. Returns
    the resulting accumulator if the loop is fixed, None otherwise.
    """

    for ptr, pair in enumerate(instructions):

        inst, n = pair

        if inst in ('nop', 'jmp'):

            # Swap jmp/nop instructions
            replacement = 'nop' if inst == 'jmp' else 'jmp'
            instructions[ptr] = [replacement, n]

            # Return accumulator if loop is fixed
            is_loop, accumulator = detect_loop(instructions)
            if not is_loop: return accumulator

            # Reset instruction back to old value
            instructions[ptr] = [inst, n]


def main():
    assert len(sys.argv) > 1, 'Missing argument: path to input file'
    assert len(sys.argv) < 3, 'Too many arguments'
    input_file = sys.argv[1]

    with open(input_file, 'r') as f:
        lines = f.read().splitlines()

    # Split instruction lines by word
    instructions = [[i, int(n)] for i, n in [i.split() for i in lines]]

    # Solve part 1
    part1 = detect_loop(instructions)[1]
    print('\nPart 1:', part1)

    # Solve part 2
    part2 = fix_program(instructions)
    print('Part 2:', part2)


if __name__ == '__main__':
    main()
