class Computer:
    def __init__(self, mem):
        self.mem = list(mem)

    def run(self):
        i = 0
        while self.mem[i] != 99:
            intcode = [0 for _ in range(5-len(str(self.mem[i])))] + [int(i) for i in str(self.mem[i])]
            i = eval('self.op_{0}(intcode, i)'.format(intcode[4]))
        return self.op_99()

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
        if intcode[2] == 0:
            self.mem[self.mem[index + 1]] = int(input('INPUT> '))
        else:
            self.mem[index + 1] = int(input('INPUT> '))
        return index + 2

    def op_4(self, intcode, index):
        print(self.get_val(intcode[2], index + 1))
        return index + 2

    def op_5(self, intcode, index):
        if self.get_val(intcode[2], index + 1) != 0:
            return self.get_val(intcode[1], index + 2)
        return index + 3

    def op_6(self, intcode, index):
        if self.get_val(intcode[2], index + 1) == 0:
            return self.get_val(intcode[1], index + 2)
        return index + 3

    def op_7(self, intcode, index):
        if self.get_val(intcode[2], index + 1) < self.get_val(intcode[1], index + 2):
            self.mem[self.mem[index + 3]] = 1
        else:
            self.mem[self.mem[index + 3]] = 0
        return index + 4

    def op_8(self, intcode, index):
        if self.get_val(intcode[2], index + 1) == self.get_val(intcode[1], index + 2):
            self.mem[self.mem[index + 3]] = 1
        else:
            self.mem[self.mem[index + 3]] = 0
        return index + 4

    def op_99(self):
        return self.mem

with open('input.txt', 'r') as f:
    mem = [int(i) for i in f.readline().split(',')]
    Computer(mem).run()
