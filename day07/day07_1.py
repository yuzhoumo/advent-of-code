import itertools
import sys

""" Day 7: Amplification Circuit

There are five amplifiers connected in series; each one receives an
input signal and produces an output signal. They are connected such that
the first amplifier's output leads to the second amplifier's input, the
second amplifier's output leads to the third amplifier's input, and so
on. The first amplifier's input value is 0, and the last amplifier's
output leads to your ship's thrusters.

The Elves have sent you some Amplifier Controller Software (your puzzle
input), a program that should run on your existing Intcode computer.
Each amplifier will need to run a copy of the program. When a copy of
the program starts running on an amplifier, it will first use an input
instruction to ask the amplifier for its current phase setting (an
integer from 0 to 4). Each phase setting is used exactly once, but the
Elves can't remember which amplifier needs which phase setting. The
program will then call another input instruction to get the amplifier's
input signal, compute the correct output signal, and supply it back to
the amplifier with an output instruction. (If the amplifier has not yet
received an input signal, it waits until one arrives.) Find the largest
output signal that can be sent to the thrusters by trying every possible
combination of phase settings on the amplifiers. Make sure that memory
is not shared or reused between copies of the program. Try every
combination of phase settings on the amplifiers. What is the highest
signal that can be sent to the thrusters? """


class AmpIntComputer:
    def __init__(self, user_inputs, memory):
        # user_inputs is a list of ints popped from each time input is
        # needed
        self.memory, self.ptr = list(memory), 0  # ptr is memory pointer
        self.inputs, self.output = user_inputs, None

    def run(self):
        while self.memory[self.ptr] != 99:
            buffer = \
                [0 for _ in range(5 - len(str(self.memory[self.ptr])))]
            code = buffer + [int(n) for n in str(self.memory[self.ptr])]
            # Executes specified opcode
            exec('self.op_{0}(code)'.format(code[4]))
        return self.op_99()

    def val(self, mode, i):
        # Returns value based on index and parameter mode
        return self.memory[i] if mode == 1 else self.memory[self.memory[i]]

    def op_1(self, code):  # opcode 1: addition
        self.memory[self.memory[self.ptr + 3]] = \
            self.val(code[2], self.ptr + 1) + self.val(code[1], self.ptr + 2)
        self.ptr += 4

    def op_2(self, code):  # opcode 2: multiplication
        self.memory[self.memory[self.ptr + 3]] = \
            self.val(code[2], self.ptr + 1) * self.val(code[1], self.ptr + 2)
        self.ptr += 4

    def op_3(self, code):  # opcode 3: take integer as input
        num = self.inputs.pop(0)
        index = self.memory[self.ptr + 1] if code[2] == 0 else self.ptr + 1
        self.memory[index], self.ptr = int(num), self.ptr + 2

    def op_4(self, code):  # opcode 4: outputs integer
        self.output = self.val(code[2], self.ptr + 1)
        self.ptr += 2

    def op_5(self, code):
        # opcode 5: if param a != 0, sets pointer position to param b
        if self.val(code[2], self.ptr + 1) != 0:
            self.ptr = self.val(code[1], self.ptr + 2)
        else:
            self.ptr += 3

    def op_6(self, code):
        # opcode 6: if param a == 0, sets pointer position to param b
        if self.val(code[2], self.ptr + 1) == 0:
            self.ptr = self.val(code[1], self.ptr + 2)
        else:
            self.ptr += 3

    def op_7(self, code):
        # opcode 7: sets memory at param c to 1 if param a < b, else
        # sets memory to 0
        if self.val(code[2], self.ptr + 1) < self.val(code[1], self.ptr + 2):
            self.memory[self.memory[self.ptr + 3]] = 1
        else:
            self.memory[self.memory[self.ptr + 3]] = 0
        self.ptr += 4

    def op_8(self, code):
        # opcode 8: sets memory at param c to 1 if param a == b, else
        # sets memory to 0
        if self.val(code[2], self.ptr + 1) == self.val(code[1], self.ptr + 2):
            self.memory[self.memory[self.ptr + 3]] = 1
        else:
            self.memory[self.memory[self.ptr + 3]] = 0
        self.ptr += 4

    def op_99(self):  # opcode 99: end
        return self.output


def amp_power(memory, phase_settings):
    output = 0
    for ps in phase_settings:
        output = AmpIntComputer([ps, output], memory).run()
    return output


def main():
    assert len(sys.argv) > 1, 'Missing argument: path to input file'
    assert len(sys.argv) < 3, 'Too many arguments'
    input_file = sys.argv[1]

    with open(input_file, 'r') as f:
        memory = tuple(int(num) for num in f.readline().split(','))

    possible_settings = list(itertools.permutations([0, 1, 2, 3, 4]))
    print(max(amp_power(memory, setting)
        for setting in possible_settings))


if __name__ == '__main__':
    main()
