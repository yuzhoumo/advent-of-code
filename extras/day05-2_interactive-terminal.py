import sys

class IntComputer:
    def __init__(self, mem):
        self.mem = list(mem)
        self.output = []

    def run(self):
        print('\n--- BEGIN EXECUTION ---\n')
        print(self.mem)
        print('\nTEST> LOADEDED MEMORY:', len(self.mem), 'BYTES')
        i, operations, output = 0, 0, []
        while i != len(self.mem):
            intcode = [0 for _ in range(5 - len(str(self.mem[i])))] + [int(i) for i in str(self.mem[i])]
            opcode, operations = intcode[3] * 10 + intcode[4], operations + 1
            print('TEST> MODES', [intcode[2], intcode[1], intcode[0]], 'OPCODE', opcode, 'POS', i)

            if opcode in range(1, 9):
                i = eval('self.op_{0}(intcode, i)'.format(opcode))
            elif opcode == 99:
                return self.op_99(operations)
            else:
                raise ValueError('OPCODE {0} not found'.format(opcode))

    def get_val(self, mode, index):
        return self.mem[index] if mode == 1 else self.mem[self.mem[index]]

    def op_1(self, intcode, index):
        a, b, c = index + 1, index + 2, self.mem[index + 3]
        self.mem[c] = self.get_val(intcode[2], a) + self.get_val(intcode[1], b)
        return index + 4

    def op_2(self, intcode, index):
        a, b, c = index + 1, index + 2, self.mem[index + 3]
        self.mem[c] = self.get_val(intcode[2], a) * self.get_val(intcode[1], b)
        return index + 4

    def op_3(self, intcode, index):
        user_input = int(input('TEST> INPUT: '))

        if intcode[2] == 0:
            self.mem[self.mem[index + 1]] = user_input
        else:
            self.mem[index + 1] = user_input
        return index + 2

    def op_4(self, intcode, index):
        self.output.append(self.get_val(intcode[2], index + 1))
        return index + 2

    def op_5(self, intcode, index):
        a, b = index + 1, index + 2
        if self.get_val(intcode[2], a) != 0:
            return self.get_val(intcode[1], b)
        return index + 3

    def op_6(self, intcode, index):
        a, b = index + 1, index + 2
        if self.get_val(intcode[2], a) == 0:
            return self.get_val(intcode[1], b)
        return index + 3

    def op_7(self, intcode, index):
        a, b, c = index + 1, index + 2, self.mem[index + 3]
        if self.get_val(intcode[2], a) < self.get_val(intcode[1], b):
            self.mem[c] = 1
        else:
            self.mem[c] = 0
        return index + 4

    def op_8(self, intcode, index):
        a, b, c = index + 1, index + 2, self.mem[index + 3]
        if self.get_val(intcode[2], a) == self.get_val(intcode[1], b):
            self.mem[c] = 1
        else:
            self.mem[c] = 0
        return index + 4

    def op_99(self, operations):
        print('\nTEST> OPERATIONS:', operations)
        print('TEST> OUTPUT:', self.output)
        print('\n--- END EXECUTION ---\n')
        self.output = []
        return self.mem


assert len(sys.argv) > 1, 'Missing argument: path to input file'
assert len(sys.argv) > 2, 'Too many arguments'

with open(sys.argv[1], 'r') as f:
    IntComputer([int(i) for i in f.readline().split(',')]).run()
