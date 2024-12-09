import aoc


def parse_disk(data):
    id, disk = 0, []
    for i in range(0, len(data) - 1, 2):
        size, free = int(data[i]), int(data[i+1])
        disk.extend([(id, size), (-1, free)])
        id += 1
    disk.append((id, int(data[-1])))
    return disk


def get_mem(disk):
    return [id for id, size in disk for _ in range(size)]


def checksum(disk):
    return sum(i * d for i, d in enumerate(disk) if d != -1)


def part1(data):
    mem = get_mem(parse_disk(data))
    res, i, j = [], 0, len(mem) - 1
    while i < j:
        while mem[j] == -1: j -= 1
        res.append(mem[i] if mem[i] != -1 else mem[j])
        i += 1
    return checksum(res)


def part2(data):
    def find_free_idx(size, end):
        for i in range(end):
            id_i, size_i = disk[i]
            if id_i == -1 and size_i >= size:
                return i

    disk = parse_disk(data)
    for j in range(len(disk) - 1, -1, -1):
        id_j, size_j = disk[j]
        if id_j == -1: continue

        i = find_free_idx(size_j, j)
        if i is None: continue

        id_i, size_i = disk[i]
        disk[i] = (id_i, size_i - size_j)
        disk[j] = (-1, size_j)
        disk.insert(i, (id_j, size_j))

    return checksum(get_mem(disk))


def main(text):
    data = text.strip()
    return part1(data), part2(data)


if __name__ == "__main__":
    aoc.run(main, 9)
