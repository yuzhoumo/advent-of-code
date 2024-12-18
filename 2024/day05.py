import aoc
from functools import cmp_to_key
from collections import defaultdict


def is_valid(rules, stack):
    seen = set()
    for n in stack:
        for after in rules[n]:
            if after in seen:
                return False
        seen.add(n)
    return True


def part1(rules, stacks):
    return sum(s[len(s)//2] for s in stacks if is_valid(rules, s))


def part2(rules, stacks):
    compare = cmp_to_key(lambda a, b: -1 if b in rules[a] else 1)
    return sum(sorted(s, key=compare)[len(s)//2] for s in stacks if not is_valid(rules, s))


def main(text):
    data = text.strip()
    rules, stacks = defaultdict(list), []

    for line in data.splitlines():
        if "|" in line:
            a, b = line.strip().split("|")
            rules[int(a)].append(int(b))
        if "," in line:
            stacks.append([int(i) for i in line.strip().split(",")])

    return part1(rules, stacks), part2(rules, stacks)


if __name__ == "__main__":
    aoc.run(main, 5)

