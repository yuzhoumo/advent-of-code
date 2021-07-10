from typing import List
import sys

""" Day 2: 1202 Program Alarm (Part 1)

An Intcode program is a list of integers separated by commas. To run
one, start by looking at the first integer (called position 0). Here,
you will find an opcode - either 1, 2, or 99. The opcode indicates what
to do. Encountering an unknown opcode means something went wrong.

- Opcode 1: adds together numbers read from two positions and stores the
  result in a third position. The three integers immediately after the
  opcode tell you these three positions - the first two indicate the
  positions from which you should read the input values, and the third
  indicates the position at which the output should be stored.

- Opcode 2: works exactly like opcode 1, except it multiplies the two
  inputs instead of adding them. Again, the three integers after the
  opcode indicate where the inputs and outputs are, not their values.

- Opcode 99: means the program is finished and should immediately halt.
  Once you're done processing an opcode, move to the next one by
  stepping forward 4 positions.

Before running the program, replace position 1 with the value 12 and
replace position 2 with the value 2. What value is left at position 0
after the program halts? """


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

    def op_99(self) -> List[int]:  # opcode 99: end
        return self.memory


def main():
    assert len(sys.argv) > 1, 'Missing argument: path to input file'
    assert len(sys.argv) > 2, ('Missing argument: IntComputer memory '
                               'value at index 1')
    assert len(sys.argv) > 3, ('Missing argument: IntComputer memory '
                               'value at index 2')
    assert len(sys.argv) < 5, 'Too many arguments'
    input_file = sys.argv[1]

    with open(input_file, 'r') as f:
        memory = [int(num) for num in f.readline().split(',')]

    # Sets memory values at index 1 & 2 with passed in args
    memory[1], memory[2] = int(sys.argv[2]), int(sys.argv[3])

    # Executes instructions in memory and prints value at index 0
    print(IntComputer(memory).run()[0])


if __name__ == '__main__':
    main()
