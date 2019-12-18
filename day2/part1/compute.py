class Computer:
    def __init__(self, mem):
        self.mem = list(mem)

    def run(self):
        i = 0
        while i < len(self.mem):
            if self.mem[i] == 1:
                self.op_one(self.mem[i+1], self.mem[i+2], self.mem[i+3])
                i += 4
            elif self.mem[i] == 2:
                self.op_two(self.mem[i+1], self.mem[i+2], self.mem[i+3])
                i += 4
            elif self.mem[i] == 99:
                return self.end()
            else:
                raise ValueError('Malformed instructions')

    def op_one(self, a, b, c):
        self.mem[c] = self.mem[a] + self.mem[b]

    def op_two(self, a, b, c):
        self.mem[c] = self.mem[a] * self.mem[b]

    def end(self):
        return self.mem


with open('input.txt', 'r') as f:
    mem = [int(i) for i in f.readline().split(',')]
    print(Computer(mem).run()[0])
