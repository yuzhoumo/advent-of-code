import aoc


def cost(a, b, target):
    b_count = (target[0] * a[1] - target[1] * a[0]) / (b[0] * a[1] - b[1] * a[0])
    a_count = (target[0] - b[0] * b_count) / a[0]
    tokens = 3 * a_count + b_count
    itokens = int(tokens)
    return itokens if itokens == tokens else 0


def part1(machines):
    return sum(cost(*m) for m in machines)


def part2(machines):
    total = 0
    for m in machines:
        x, y = m[2]
        total += cost(m[0], m[1], (x + 10000000000000, y + 10000000000000))
    return total


def main(text):
    data = text.strip()
    parsed = []
    entry = []

    for line in data.splitlines():
        if len(entry) == 3:
            parsed.append(entry)
            entry = []
        if line.strip() == "":
            continue
        if line.startswith("Button"):
            line = line[len("Button X:"):]
        if line.startswith("Prize"):
            line = line[len("Prize:"):]

        x, y = line.split(",")
        entry.append((int(x[3:]), int(y[3:])))

    if entry:
        parsed.append(entry)

    return part1(parsed), part2(parsed)


if __name__ == "__main__":
    aoc.run(main, 13)
