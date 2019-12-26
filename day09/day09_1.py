import sys

""" Day 9: Sensor Boost (Part 1)

Your existing Intcode computer is missing one key feature: it needs support for parameters in relative mode. Parameters
in mode 2, relative mode, behave very similarly to parameters in position mode: the parameter is interpreted as a
position. Like position mode, parameters in relative mode can be read from or written to.

The important difference is that relative mode parameters don't count from address 0. Instead, they count from a value
called the relative base. The relative base starts at 0. The address a relative mode parameter refers to is itself plus
the current relative base. When the relative base is 0, relative mode parameters and position mode parameters with the
same value refer to the same address.

The relative base is modified with the relative base offset instruction:

- Opcode 9: adjusts the relative base by the value of its only parameter. The relative base increases (or decreases,
  if the value is negative) by the value of the parameter.

Your Intcode computer will also need a few other capabilities:

The computer's available memory should be much larger than the initial program. Memory beyond the initial program starts
with the value 0 and can be read or written like any other memory. (It is invalid to try to access memory at a negative
address, though.) The computer should have support for large numbers. Some instructions near the beginning of the BOOST
program will verify this capability.

The BOOST program will ask for a single input; run it in test mode by providing it the value 1. It will perform a series
of checks on each opcode, output any opcodes (and the associated parameter modes) that seem to be functioning
incorrectly, and finally output a BOOST keycode. The BOOST program should report no malfunctioning opcodes when run in
test mode; it should only output a single value, the BOOST keycode. What BOOST keycode does it produce? """


class IntComputer:
    def __init__(self, user_inputs, memory):  # user_inputs is a list of ints popped from each time input is needed
        self.memory = dict(zip(range(len(memory)), memory))  # Convert list to dict with indices as keys
        self.ptr = self.relative_base = 0 # self.ptr is memory pointer
        self.inputs, self.outputs = list(user_inputs), []

    def run(self):
        while self.get_memory(self.ptr) != 99:
            buffer = [0 for _ in range(5 - len(str(self.get_memory(self.ptr))))]
            code = buffer + [int(n) for n in str(self.get_memory(self.ptr))]
            exec('self.op_{0}(code)'.format(code[4]))  # Executes specified opcode
        return self.op_99()

    def get_memory(self, index):  # Gets memory at specified index even if index > len(self.memory)
        assert index >= 0, 'Cannot get value at negative memory position'
        result = self.memory.get(index, None)
        if not result:
            self.memory[index] = 0
            return 0
        return result

    def set_memory(self, index, value):  # Sets memory at specified index even if index > len(self.memory)
        assert index >= 0, 'Cannot set value at negative memory position'
        self.memory[index] = value

    def val(self, mode, i):  # Returns value based on index and parameter mode
        if mode == 0:
            return self.get_memory(self.get_memory(i))
        if mode == 1:
            return self.get_memory(i)
        if mode == 2:
            return self.get_memory(self.relative_base + self.get_memory(i))
        raise ValueError('Invalid mode: {0}'.format(mode))

    def index_val(self, mode, i):  # Returns index value based on parameter mode
        if mode == 0:
            return self.get_memory(i)
        if mode == 2:
            return self.relative_base + self.get_memory(i)
        raise ValueError('Invalid mode: {0}'.format(mode))

    def op_1(self, code):  # opcode 1: addition
        self.set_memory(self.index_val(code[0], self.ptr + 3),
                        self.val(code[2], self.ptr + 1) + self.val(code[1], self.ptr + 2))
        self.ptr += 4

    def op_2(self, code):  # opcode 2: multiplication
        self.set_memory(self.index_val(code[0], self.ptr + 3),
                        self.val(code[2], self.ptr + 1) * self.val(code[1], self.ptr + 2))
        self.ptr += 4

    def op_3(self, code):  # opcode 3: take integer as input
        assert len(self.inputs) > 0, 'Expected input but self.inputs was empty'
        num = self.inputs.pop(0)
        self.set_memory(self.index_val(code[2], self.ptr + 1), int(num))
        print('INPUT>', num)
        self.ptr += 2

    def op_4(self, code):  # opcode 4: outputs integer
        output = self.val(code[2], self.ptr + 1)
        print('OUTPUT', output)
        self.outputs.append(output)
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
            self.set_memory(self.index_val(code[0], self.ptr + 3), 1)
        else:
            self.set_memory(self.index_val(code[0], self.ptr + 3), 0)
        self.ptr += 4

    def op_8(self, code):  # opcode 8: sets memory at param c to 1 if param a == b, else sets memory to 0
        if self.val(code[2], self.ptr + 1) == self.val(code[1], self.ptr + 2):
            self.set_memory(self.index_val(code[0], self.ptr + 3), 1)
        else:
            self.set_memory(self.index_val(code[0], self.ptr + 3), 0)
        self.ptr += 4

    def op_9(self, code):  # opcode 9: modify relative base
        self.relative_base += self.val(code[2], self.ptr + 1)
        self.ptr += 2

    def op_99(self):  # opcode 99: end
        return self.outputs


def main():
    assert len(sys.argv) > 1, 'Missing argument: path to input file'
    assert len(sys.argv) > 2, 'Missing arguments: user input'
    input_file = sys.argv[1]

    with open(input_file, 'r') as f:
        user_inputs = [int(num) for num in sys.argv[2:]]
        memory = tuple(int(num) for num in f.readline().split(','))

    IntComputer(user_inputs, memory).run()


if __name__ == '__main__':
    main()
