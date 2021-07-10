import sys
import re


def parse_instructions(raw):
    """
    Parse raw input into a list of tuples in either of the following formats:
        ('mask', '1101000X0110100X1X1X00001010XX00X0X0')
        ('mem', 48482, 6450058)
    """

    pattern, parsed = re.compile(r'(mask|mem)\[*(\d+)?\]* = (.+)'), []

    for match in pattern.findall(raw):
        match = filter(None, match)
        match = tuple(map(lambda m: int(m) if m.isnumeric() else m, match))
        parsed.append(match)

    return parsed


# Part 1
def compute_sum_maskval(instructions):
    """
    Execute the given list of instructions and return the sum of all the values
    in memory. Instructions either set the value of the mask or write a masked
    value to a location in memory.

    Example:

        value:  000000000000000000000000000000001011  (decimal 11)
        mask:   XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
        result: 000000000000000000000000000001001001  (decimal 73)
    """

    mask, mem = '', {}
    masker = lambda mask_bit, c: c if mask_bit == 'X' else mask_bit

    for inst in instructions:
        if inst[0] == 'mask':
            mask = inst[1]
        elif inst[0] == 'mem':
            bin_val = str(bin(inst[2]))[2:]
            padded = '0' * (len(mask) - len(bin_val)) + bin_val

            res = ''
            for i, mask_bit in enumerate(mask):
                res += masker(mask_bit, padded[i])

            mem[inst[1]] = res

    return sum(int(v, 2) for v in mem.values())


# Part 2
def get_addresses(mask, padded):
    """
    Takes in a mask and zero-padded memory address of the same length and return
    a list of all the possible memory addresses after applying the mask.
    
    Example:

        address: 000000000000000000000000000000101010  (decimal 42)
        mask:    000000000000000000000000000000X1001X
        result:  000000000000000000000000000000X1101X

        floating bits 'X' take on all possible values:

        000000000000000000000000000000010000  (decimal 16)
        000000000000000000000000000000010001  (decimal 17)
        000000000000000000000000000000010010  (decimal 18)
        000000000000000000000000000000010011  (decimal 19)
        000000000000000000000000000000011000  (decimal 24)
        000000000000000000000000000000011001  (decimal 25)
        000000000000000000000000000000011010  (decimal 26)
        000000000000000000000000000000011011  (decimal 27)
    """

    results, curr = [''], ''

    for i, m in enumerate(mask):
        if m == '0':    # Pass through the original bit
            curr += padded[i]
        elif m == '1':  # Overwrite original bit with '1'
            curr += '1'
        elif m == 'X':  # Add both possible floating bits
            copy = results[:]

            for j in range(len(results)):
                results[j] += curr + '0'
                copy[j] += curr + '1'

            results.extend(copy)
            curr = ''

    if curr:  # Add remaining bits from curr if curr is not empty
        for i in range(len(results)):
            results[i] += curr

    return results


def compute_sum_maskmem(instructions):
    """
    Execute the given list of instructions and return the sum of all the values
    in memory. Instructions either set the value of the mask or write the values
    to a masked memory address.
    """

    mask, mem = '', {}

    for inst in instructions:
        if inst[0] == 'mask':
            mask = inst[1]
        elif inst[0] == 'mem':
            bin_addr = str(bin(inst[1]))[2:]
            padded = '0' * (len(mask) - len(bin_addr)) + bin_addr
            for a in get_addresses(mask, padded):
                mem[a] = inst[2]

    return sum(mem.values())


def main():
    assert len(sys.argv) > 1, 'Missing argument: path to input file'
    assert len(sys.argv) < 3, 'Too many arguments'
    input_file = sys.argv[1]

    with open(input_file, 'r') as f:
        instructions = parse_instructions(f.read())

    # Solve part 1
    part1 = compute_sum_maskval(instructions)
    print('\nPart 1:', part1)

    # Solve part 2
    part2 = compute_sum_maskmem(instructions)
    print('Part 2:', part2)


if __name__ == '__main__':
    main()
