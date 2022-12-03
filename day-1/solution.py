with open("input.txt") as f:
    elfs = [
        [int(cal) for cal in e.strip().split("\n")]
        for e in f.read().strip().split("\n\n")
    ]

print("Part 1", max(sum(elf) for elf in elfs))
print("Part 2", sum(sorted(sum(elf) for elf in elfs)[-3:]))
