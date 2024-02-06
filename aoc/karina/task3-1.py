import re


def part1(data):
    nums, symbols = parse_input(data)
    adj_nums = []
    for pos, _ in symbols.items():
        r, c = pos
        adj_pos = [(r + x, c + y) for x in [-1, 0, 1] for y in [-1, 0, 1]]
        adj_nums.extend([nums[pos] for pos in adj_pos if pos in nums])
    return sum(item[0] for item in set(adj_nums))


def parse_input(data):
    nums = {}
    syms = {}
    idx_num = 0

    for r, line in enumerate(data):
        line_nums = re.sub(r"\D", " ", line).split()
        offset = 0
        for n in line_nums:
            pos = line.index(n, offset)
            for step in range(len(n)):
                nums[(r, pos + step)] = (int(n), idx_num)
            offset = pos + len(n)
            idx_num += 1

        line_syms = re.sub(r"[\d\.]", " ", line).split()
        offset = 0
        for sym in line_syms:
            pos = line.index(sym, offset)
            syms[(r, pos)] = sym
            offset = pos + 1

    return nums, syms


with open('input2-1.txt', 'r') as file:
    lines = file.readlines()
    print(part1(lines))
