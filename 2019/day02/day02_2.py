import sys

""" Day 2: 1202 Program Alarm (Part 2)

To complete the gravity assist, you need to determine what pair of
inputs produces the output 19690720. The inputs should still be provided
to the program by replacing the values at addresses 1 and 2, just like
before. In this program, the value placed in address 1 is called the
noun, and the value placed in address 2 is called the verb. Each of the
two input values will be between 0 and 99, inclusive.

Once the program has halted, its output is available at address 0, also
just like before. Each time you try a pair of inputs, make sure you
first reset the computer's memory to the values in the program (your
puzzle input) - in other words, don't reuse memory from a previous
attempt.

Find the input noun and verb that cause the program to produce the
output 19690720. What is 100 * noun + verb? (For example, if noun=12 and
verb=2, the answer would be 1202.) """


class IntComputer:
    def __init__(self, memory):
        self.memory = list(memory)
        self.ptr = 0  # self.ptr is memory pointer

    def run(self):
        while self.ptr < len(self.memory):
            if self.memory[self.ptr] == 1:
                self.op_1(self.memory[self.ptr + 1],
                          self.memory[self.ptr + 2],
                          self.memory[self.ptr + 3])
                self.ptr += 4
            elif self.memory[self.ptr] == 2:
                self.op_2(self.memory[self.ptr + 1],
                          self.memory[self.ptr + 2],
                          self.memory[self.ptr + 3])
                self.ptr += 4
            elif self.memory[self.ptr] == 99:
                return self.op_99()
            else:
                raise ValueError('Unknown opcode: {0}'
                                .format(self.memory[self.ptr]))
        return self.op_99()

    def op_1(self, a, b, c):  # opcode 1: addition operation
        self.memory[c] = self.memory[a] + self.memory[b]

    def op_2(self, a, b, c):  # opcode 2: multiplication operation
        self.memory[c] = self.memory[a] * self.memory[b]

    def op_99(self):  # opcode 99: end
        return self.memory


def find_inputs(result, memory):
    # Finds inputs to IntComputer that cause it to yield result variable
    memory = list(memory)
    # Inputs can be only values from 1-99
    for input1 in range(0, 100):
        for input2 in range(0, 100):
            # Sets inputs by mutating memory at indices 1 and 2
            memory[1], memory[2] = input1, input2
            if IntComputer(memory).run()[0] == result:
                return 100 * input1 + input2


def main():
    assert len(sys.argv) > 1, 'Missing argument: path to input file'
    assert len(sys.argv) > 2, ('Missing argument: expected output '
                               'integer of IntComputer')
    assert len(sys.argv) < 4, 'Too many arguments'
    input_file, result = sys.argv[1], int(sys.argv[2])

    with open(input_file, 'r') as f:
        memory = [int(num) for num in f.readline().split(',')]

    print(find_inputs(result, memory))


if __name__ == '__main__':
    main()
