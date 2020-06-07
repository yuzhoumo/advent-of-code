import sys

""" Day 5: Sunny with a Chance of Asteroids (Part 2)

Your computer is only missing a few opcodes:

- Opcode 5: is jump-if-true: if the first parameter is non-zero, it sets
  the instruction pointer to the value from the second parameter.
  Otherwise, it does nothing.
- Opcode 6: is jump-if-false: if the first parameter is zero, it sets
  the instruction pointer to the value from the second parameter.
  Otherwise, it does nothing.
- Opcode 7: is less than: if the first parameter is less than the second
  parameter, it stores 1 in the position given by the third parameter.
  Otherwise, it stores 0.
- Opcode 8: is equals: if the first parameter is equal to the second
  parameter, it stores 1 in the position given by the third parameter.
  Otherwise, it stores 0.

Like all instructions, these instructions need to support parameter
modes as described above. Normally, after an instruction is finished,
the instruction pointer increases by the number of values in that
instruction. However, if the instruction modifies the instruction
pointer, that value is used and the instruction pointer is not
automatically increased. When the TEST diagnostic program runs its input
instruction to get the ID of the system to test, provide it 5, the ID
for the ship's thermal radiator controller. This diagnostic test suite
only outputs one number, the diagnostic code. What is the diagnostic
code for system ID 5? """


class IntComputer:
    def __init__(self, user_inputs, memory): 
        # user_inputs is a list of ints popped from each time input is
        # needed
        self.memory = list(memory)
        self.ptr = 0  # self.ptr is memory pointer
        self.inputs, self.outputs = list(user_inputs), []

    def run(self):
        while self.memory[self.ptr] != 99:
            buffer = [0 for _ in range(5 - len(str(self.memory[self.ptr])))]
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
        print('INPUT>', num)

    def op_4(self, code):  # opcode 4: outputs integer
        output, self.ptr = self.val(code[2], self.ptr + 1), self.ptr + 2
        print('OUTPUT', output)
        self.outputs.append(output)

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
        return self.outputs


def main():
    assert len(sys.argv) > 1, 'Missing argument: path to input file'
    assert len(sys.argv) > 2, 'Missing argument: IntComputer user input'
    input_file = sys.argv[1]

    with open(input_file, 'r') as f:
        user_input = [num for num in sys.argv[2:]]
        memory = [int(num) for num in f.readline().split(',')]

    IntComputer(user_input, memory).run()


if __name__ == '__main__':
    main()
