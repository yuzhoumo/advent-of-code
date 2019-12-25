import itertools
import sys

""" Day 7: Amplification Circuit (Part 2)

Most of the amplifiers are connected as they were before; amplifier A's output is connected to amplifier B's input, and
so on. However, the output from amplifier E is now connected into amplifier A's input. This creates the feedback loop:
the signal will be sent through the amplifiers many times.

In feedback loop mode, the amplifiers need totally different phase settings: integers from 5 to 9, again each used
exactly once. These settings will cause the Amplifier Controller Software to repeatedly take input and produce output
many times before halting. Provide each amplifier its phase setting at its first input instruction; all further
input/output instructions are for signals. Don't restart the Amplifier Controller Software on any amplifier during this
process. Each one should continue receiving and sending signals until it halts. All signals sent or received in this
process will be between pairs of amplifiers except the very first signal and the very last signal. To start the process,
a 0 signal is sent to amplifier A's input exactly once.

Eventually, the software on the amplifiers will halt after they have processed the final loop. When this happens, the
last output signal from amplifier E is sent to the thrusters. Your job is to find the largest output signal that can be
sent to the thrusters using the new phase settings and feedback loop arrangement. Try every combination of the new phase
settings on the amplifier feedback loop. What is the highest signal that can be sent to the thrusters? """


class AmpIntComputer:
    def __init__(self, user_inputs, memory):  # user_inputs is a list of ints popped from each time input is needed
        self.memory, self.ptr = list(memory), 0  # ptr is memory pointer
        self.inputs, self.output = user_inputs, None

    def run(self):
        while self.ptr < len(self.memory) and self.memory[self.ptr] != 99:
            buffer = [0 for _ in range(5 - len(str(self.memory[self.ptr])))]
            code = buffer + [int(i) for i in str(self.memory[self.ptr])]
            exec('self.op_{0}(code)'.format(code[4]))  # Executes specified opcode

            if code[4] == 4:
                return self.output

        return None  # opcode 99: end

    def val(self, mode, i):  # Returns value based on index and parameter mode
        return self.memory[i] if mode == 1 else self.memory[self.memory[i]]

    def op_1(self, code):  # opcode 1: addition
        self.memory[self.memory[self.ptr + 3]] = self.val(code[2], self.ptr + 1) + self.val(code[1], self.ptr + 2)
        self.ptr += 4

    def op_2(self, code):  # opcode 2: multiplication
        self.memory[self.memory[self.ptr + 3]] = self.val(code[2], self.ptr + 1) * self.val(code[1], self.ptr + 2)
        self.ptr += 4

    def op_3(self, code):  # opcode 3: take integer as input
        # Pops first item in self.inputs (phase setting) if length is > 1
        num = self.inputs.pop(0) if len(self.inputs) > 1 else self.inputs[0]
        index = self.memory[self.ptr + 1] if code[2] == 0 else self.ptr + 1
        self.memory[index], self.ptr = int(num), self.ptr + 2

    def op_4(self, code):  # opcode 4: sets self.output
        self.output = self.val(code[2], self.ptr + 1)
        self.ptr += 2

    def op_5(self, code):  # opcode 5: if param a != 0, sets pointer position to param b
        if self.val(code[2], self.ptr + 1) != 0:
            self.ptr = self.val(code[1], self.ptr + 2)
        else:
            self.ptr += 3

    def op_6(self, code):  # opcode 6: if param a == 0, sets pointer position to param b
        if self.val(code[2], self.ptr + 1) == 0:
            self.ptr = self.val(code[1], self.ptr + 2)
        else:
            self.ptr += 3

    def op_7(self, code):  # opcode 7: sets memory at param c to 1 if param a < b, else sets memory to 0
        if self.val(code[2], self.ptr + 1) < self.val(code[1], self.ptr + 2):
            self.memory[self.memory[self.ptr + 3]] = 1
        else:
            self.memory[self.memory[self.ptr + 3]] = 0
        self.ptr += 4

    def op_8(self, code):  # opcode 8: sets memory at param c to 1 if param a == b, else sets memory to 0
        if self.val(code[2], self.ptr + 1) == self.val(code[1], self.ptr + 2):
            self.memory[self.memory[self.ptr + 3]] = 1
        else:
            self.memory[self.memory[self.ptr + 3]] = 0
        self.ptr += 4


def amp_power(memory, phase_settings):
    amps = [AmpIntComputer([ps, None], memory) for ps in phase_settings]
    count = output = prev = 0

    while output is not None:
        count = count + 1 if count < len(amps) - 1 else 0

        if len(amps[count].inputs) < 2:  # If phase setting has been popped from self.inputs
            amps[count].inputs[0] = output
        else:
            amps[count].inputs[1] = output

        prev, output = output, amps[count].run()

    return prev


def main():
    assert len(sys.argv) > 1, 'Missing argument: path to input file'
    assert len(sys.argv) < 3, 'Too many arguments'
    input_file = sys.argv[1]

    with open(input_file, 'r') as f:
        memory = tuple(int(i) for i in f.readline().split(','))

    possible_settings = list(itertools.permutations([5, 6, 7, 8, 9]))
    print(max(amp_power(memory, setting) for setting in possible_settings))


if __name__ == '__main__':
    main()
