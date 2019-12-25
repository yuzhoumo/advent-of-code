import sys


class IntComputer:
    def __init__(self, mem):
        self.mem = list(mem)
        self.relative_base = 0

    def run(self):
        i = 0
        while self.mem[i] != 99:
            buffer = [0 for _ in range(5 - len(str(self.mem[i])))]
            code = buffer + [int(i) for i in str(self.mem[i])]
            i = eval('self.op_{0}(code,i)'.format(code[4]))
        return self.op_99()

    def val(self, mode, i):
        return self.mem[i] if mode == 1 else self.mem[self.mem[i]]

    def op_1(self, code, i):
        self.mem[self.mem[i + 3]] = self.val(code[2], i + 1) + self.val(code[1], i + 2)
        return i + 4

    def op_2(self, code, i):
        self.mem[self.mem[i + 3]] = self.val(code[2], i + 1) * self.val(code[1], i + 2)
        return i + 4

    def op_3(self, code, i):
        num = user_input.pop(0)
        if code[2] == 0:
            self.mem[self.mem[i + 1]] = int(num)
        else:
            self.mem[i + 1] = int(num)
        print('INPUT>', num)
        return i + 2

    def op_4(self, code, i):
        print('OUTPUT', self.val(code[2], i + 1))
        return i + 2

    def op_5(self, code, i):
        if self.val(code[2], i + 1) != 0:
            return self.val(code[1], i + 2)
        return i + 3

    def op_6(self, code, i):
        if self.val(code[2], i + 1) == 0:
            return self.val(code[1], i + 2)
        return i + 3

    def op_7(self, code, i):
        if self.val(code[2], i + 1) < self.val(code[1], i + 2):
            self.mem[self.mem[i + 3]] = 1
        else:
            self.mem[self.mem[i + 3]] = 0
        return i + 4

    def op_8(self, code, i):
        if self.val(code[2], i + 1) == self.val(code[1], i + 2):
            self.mem[self.mem[i + 3]] = 1
        else:
            self.mem[self.mem[i + 3]] = 0
        return i + 4

    def op_9(self, code, i):
        self.relative_base += self.val(code[2], i + 1)

    def op_99(self):
        return self.mem


def main():
    # Assertions for handling args passed in through command line
    assert len(sys.argv) > 1, 'Missing argument: path to input file'
    assert len(sys.argv) > 2, 'Missing argument: IntComputer user input'

    with open(sys.argv[1], 'r') as f:
        user_input = [n for n in sys.argv[2:]]
        IntComputer([int(i) for i in f.readline().split(',')]).run()


if __name__ == '__main__':
    main()
