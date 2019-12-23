import sys


class IntComputer:
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


assert len(sys.argv) > 1, 'Missing argument: path to input file'
assert len(sys.argv) > 2, 'Missing argument: intcomputer memory at index 1'
assert len(sys.argv) > 3, 'Missing argument: intcomputer memory at index 2'
assert len(sys.argv) < 5, 'Too many arguments'

with open(sys.argv[1], 'r') as f:
    mem = [int(i) for i in f.readline().split(',')]

mem[1], mem[2] = int(sys.argv[2]), int(sys.argv[3])
print(IntComputer(mem).run()[0])
