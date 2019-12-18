class Computer:
    def __init__(self, mem):
        self.mem = list(mem)

    def run(self):
        print('\n--- BEGIN EXECUTION ---\n')
        print('TEST> LOADEDED MEMORY:', len(self.mem), 'BYTES')
        i, output = 0, []
        while i < len(self.mem):
            intcode = [0 for _ in range(5-len(str(self.mem[i])))] + [int(i) for i in str(self.mem[i])]
            opcode = intcode[3] * 10 + intcode[4]
            print('TEST> POS', i, 'INTCODE', intcode, 'OPCODE', opcode)

            if opcode == 1:
                self.op_one(intcode, i)
                i += 4
            elif opcode == 2:
                self.op_two(intcode, i)
                i += 4
            elif opcode == 3:
                self.op_three(intcode, i)
                i += 2
            elif opcode == 4:
                self.op_four(intcode, i, output)
                i += 2
            elif opcode == 99:
                return self.end(output)
            else:
                raise ValueError('Malformed instructions')

    def get_val(self, mode, index):
        return self.mem[index] if mode == 1 else self.mem[self.mem[index]]

    def op_one(self, intcode, index):
        a, b, c = index + 1, index + 2, self.mem[index + 3]
        self.mem[c] = self.get_val(intcode[2], a) + self.get_val(intcode[1], b)

    def op_two(self, intcode, index):
        a, b, c = index + 1, index + 2, self.mem[index + 3]
        self.mem[c] = self.get_val(intcode[2], a) * self.get_val(intcode[1], b)

    def op_three(self, intcode, index):
        user_input = int(input('TEST> INPUT: '))

        if intcode[2] == 0:
            self.mem[self.mem[index + 1]] = user_input
        else:
            self.mem[index + 1] = user_input

    def op_four(self, intcode, index, output):
        output.append(self.get_val(intcode[2], index + 1))

    def end(self, output):
        print()
        [print('TEST> OUPUT:', out) for out in output]
        print('\n--- END EXECUTION ---\n')
        return self.mem

with open('input.txt', 'r') as f:
    mem = [int(i) for i in f.readline().split(',')]
    Computer(mem).run()
