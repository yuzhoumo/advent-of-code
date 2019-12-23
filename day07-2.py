import itertools
import sys


class AmpIntComputer:
    def __init__(self, mem, phase_setting, amp_input):
        self.mem, self.ptr = list(mem), 0
        self.input, self.phase_setting = amp_input, [phase_setting]

    def run(self):
        while self.ptr < len(self.mem) and self.mem[self.ptr] != 99:
            buffer = [0 for _ in range(5 - len(str(self.mem[self.ptr])))]
            code = buffer + [int(i) for i in str(self.mem[self.ptr])]
            self.ptr = eval('self.op_{0}(code, self.ptr)'.format(code[4]))

            if code[4] == 4:
                return self.output

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
        num = self.phase_setting.pop(0) if len(self.phase_setting) > 0 else self.input
        if code[2] == 0:
            self.mem[self.mem[i + 1]] = int(num)
        else:
            self.mem[i + 1] = int(num)
        return i + 2

    def op_4(self, code, i):
        self.output = (self.val(code[2], i + 1))
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

    def op_99(self):
        return None


def amp_power(computer_memory, phase_settings):
    amps = [AmpIntComputer(computer_memory, ps, None) for ps in phase_settings]
    count = output = prev = 0

    while output is not None:
        count, prev = count + 1 if count < len(amps) - 1 else 0, output
        amps[count].input = prev
        output = amps[count].run()

    return prev


assert len(sys.argv) > 1, 'Missing argument: path to input file'
assert len(sys.argv) < 3, 'Too many arguments'

with open(sys.argv[1], 'r') as f:
    memory = tuple(int(i) for i in f.readline().split(','))

possible = list(itertools.permutations([5, 6, 7, 8, 9]))
print(max(amp_power(memory, setting) for setting in possible))
