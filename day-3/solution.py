with open("input.txt") as f:
    rucksacks = [
        (stripped[: len(stripped) // 2], stripped[len(stripped) // 2 :])
        for e in f.readlines()
        if (stripped := e.strip())
    ]


def letter_to_priority(letter: str) -> int:
    if "a" <= letter <= "z":
        return ord(letter) - ord("a") + 1
    if "A" <= letter <= "Z":
        return ord(letter) - ord("A") + 1 + 26
    raise ValueError("Invalid letter")


def part1(data: list[tuple[str, str]]) -> int:
    prio_sum = 0
    for left, right in data:
        common = (set(left) & set(right)).pop()
        prio_sum += letter_to_priority(common)

    return prio_sum


def part2(data: list[tuple[str, str]]) -> int:
    prio_sum = 0
    for i in range(len(data) // 3):
        sacks = list(map(set, map(lambda p: p[0] + p[1], data[i * 3 : i * 3 + 3])))
        for s in sacks:
            sacks[0] &= s

        prio_sum += letter_to_priority(sacks[0].pop())

    return prio_sum


print("Part 1", part1(rucksacks))
print("Part 2", part2(rucksacks))
