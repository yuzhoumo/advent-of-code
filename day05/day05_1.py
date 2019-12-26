import sys

""" Day 5: Sunny with a Chance of Asteroids (Part 1)

The Thermal Environment Supervision Terminal (TEST) starts by running a diagnostic program (your puzzle input). 
The TEST diagnostic program will run on your existing Intcode computer after a few modifications. First, you'll need to
add two new instructions:

- Opcode 3: takes a single integer as input and saves it to the position given by its only parameter. For example,
  the instruction 3,50 would take an input value and store it at address 50.
- Opcode 4: outputs the value of its only parameter. For example, the instruction 4,50 would output the value at
  address 50.

Second, you'll need to add support for parameter modes:

Each parameter of an instruction is handled based on its parameter mode. Right now, your ship computer already
understands parameter mode 0, position mode, which causes the parameter to be interpreted as a position - if the
parameter is 50, its value is the value stored at address 50 in memory. Until now, all parameters have been in position
mode. Your ship computer will also need to handle parameters in mode 1, immediate mode. In immediate mode, a parameter
is interpreted as a value - if the parameter is 50, its value is simply 50.

Parameter modes are stored in the same value as the instruction's opcode. The opcode is a two-digit number based only on
the ones and tens digit of the value, that is, the opcode is the rightmost two digits of the first value in an
instruction. Parameter modes are single digits, one per parameter, read right-to-left from the opcode: the first
parameter's mode is in the hundreds digit, the second parameter's mode is in the thousands digit, the third parameter's
mode is in the ten-thousands digit, and so on. Any missing modes are 0.

It is important to remember that the instruction pointer should increase by the number of values in the instruction
after the instruction finishes. Because of the new instructions, this amount is no longer always 4. Integers can be
negative: 1101,100,-1,4,0 is a valid program (find 100 + -1, store the result in position 4).

The TEST diagnostic program will start by requesting from the user the ID of the system to test by running an input
instruction - provide it 1, the ID for the ship's air conditioner unit. It will then perform a series of diagnostic
tests confirming that various parts of the Intcode computer, like parameter modes, function correctly. For each test,
it will run an output instruction indicating how far the result of the test was from the expected value, where 0 means
the test was successful. Non-zero outputs mean that a function is not working correctly; check the instructions that
were run before the output instruction to see which one failed.

Finally, the program will output a diagnostic code and immediately halt. This final output isn't an error; an output
followed immediately by a halt means the program finished. If all outputs were zero except the diagnostic code,
the diagnostic program ran successfully. After providing 1 to the only input instruction and passing all the tests,
what diagnostic code does the program produce? """


class IntComputer:
    def __init__(self, user_inputs, memory):  # user_inputs is a list of ints popped from each time input is needed
        self.memory, self.ptr = list(memory), 0  # self.ptr is memory pointer
        self.inputs = list(user_inputs)

    def run(self):
        while self.ptr < len(self.memory) and self.memory[self.ptr] != 99:
            buffer = [0 for _ in range(5 - len(str(self.memory[self.ptr])))]
            code = buffer + [int(i) for i in str(self.memory[self.ptr])]
            exec('self.op_{0}(code)'.format(code[4]))  # Executes specified opcode
        return self.op_99()

    def val(self, mode, i):  # Returns value based on index and parameter mode
        return self.memory[i] if mode == 1 else self.memory[self.memory[i]]

    def op_1(self, code):  # opcode 1: addition
        self.memory[self.memory[self.ptr + 3]] = self.val(code[2], self.ptr + 1) + self.val(code[1], self.ptr + 2)
        self.ptr += 4

    def op_2(self, code):  # opcode 2: multiplication
        self.memory[self.memory[self.ptr + 3]] = self.val(code[2], self.ptr + 1) * self.val(code[1], self.ptr + 2)
        self.ptr += 4

    def op_3(self, code):  # opcode 3: take integer as input
        num, index = self.inputs.pop(0), self.memory[self.ptr + 1] if code[2] == 0 else self.ptr + 1
        self.memory[index], self.ptr = num, self.ptr + 2
        print('INPUT>', num)

    def op_4(self, code):  # opcode 4: outputs integer
        output, self.ptr = self.val(code[2], self.ptr + 1), self.ptr + 2
        print('OUTPUT', output)

    def op_99(self):  # opcode 99: end
        return self.memory


def main():
    assert len(sys.argv) > 1, 'Missing argument: path to input file'
    assert len(sys.argv) > 2, 'Missing argument: IntComputer user input'
    input_file = sys.argv[1]

    with open(input_file, 'r') as f:
        user_input, memory = [int(num) for num in sys.argv[2:]], [int(num) for num in f.readline().split(',')]

    IntComputer(user_input, memory).run()


if __name__ == '__main__':
    main()
