import aoc


def compact(disk):
    res = []
    i = 0
    while i < len(disk):
        while disk[-1] is None:
            disk.pop()
        if disk[i] is not None:
            res.append(disk[i])
        else:
            res.append(disk.pop())
        i += 1
    return res


def checksum(disk):
    checksum = 0
    for i, d in enumerate(disk):
        if d != -1:
            checksum += i * d
    return checksum


def parse_disk(data):
    id = 0
    disk = []
    for i in range(0, len(data) - 1, 2):
        size, free = int(data[i]), int(data[i+1])
        disk.extend([id] * size)
        disk.extend([None] * free)
        id += 1
    disk.extend([id] * int(data[-1]))
    return disk


def parse_disk2(data):
    id = 0
    disk = []
    for i in range(0, len(data) - 1, 2):
        size, free = int(data[i]), int(data[i+1])
        disk.append((id, size))
        disk.append((-1, free))
        id += 1
    disk.append((id, int(data[-1])))
    return disk


def part1(data):
    res = compact(parse_disk(data))
    return checksum(res)


def part2(data):
    disk = parse_disk2(data)
    for j in range(len(disk) - 1, -1, -1):
        ij, sj = disk[j]
        if ij == -1: continue

        for i in range(j):
            ii, si = disk[i]
            if ii != -1: continue

            if si > sj:
                disk[i] = (ii, si - sj)
                disk[j] = (-1, sj)
                disk.insert(i, (ij, sj))
                break
            elif si == sj:
                disk[j] = (-1, sj)
                disk[i] = (ij, sj)
                break

    res = []
    for d in disk:
        res.extend([d[0]] * d[1])

    return checksum(res)


def main(text):
    data = text.strip()
    return part1(data), part2(data)


if __name__ == "__main__":
    aoc.run(main, 9)
