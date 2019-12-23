import sys


class Computer:
    def __init__(self, memory):
        self.memory = list(memory)

    def run(self):
        i = 0
        while i < len(self.memory):
            if self.memory[i] == 1:
                self.op_1(self.memory[i + 1], self.memory[i + 2], self.memory[i + 3])
                i += 4
            elif self.memory[i] == 2:
                self.op_2(self.memory[i + 1], self.memory[i + 2], self.memory[i + 3])
                i += 4
            elif self.memory[i] == 99:
                return self.op_99()
            else:
                raise ValueError('Malformed instructions')

    def op_1(self, a, b, c):
        self.memory[c] = self.memory[a] + self.memory[b]

    def op_2(self, a, b, c):
        self.memory[c] = self.memory[a] * self.memory[b]

    def op_99(self):
        return self.memory


def find_inputs(result, memory):
    for i in range(0, 100):
        for j in range(0, 100):
            memory[1], memory[2] = i, j
            if Computer(memory).run()[0] == result:
                return 100 * i + j


assert len(sys.argv) > 1, 'Missing argument: path to input file'
assert len(sys.argv) > 2, 'Missing argument: output integer of IntComputer'
assert len(sys.argv) < 4, 'Too many arguments'

with open(sys.argv[1], 'r') as f:
    print(find_inputs(int(sys.argv[2]), [int(i) for i in f.readline().split(',')]))
