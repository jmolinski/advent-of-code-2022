with open("input.txt") as f:
    pairs = [
        [[int(n) for n in e.split("-")] for e in l.strip().split(",")]
        for l in f.readlines()
    ]

fully_enclosed = 0
partially_enclosed = 0
for [(l1, r1), (l2, r2)] in pairs:
    if (l1 <= l2 <= r1 and l1 <= r2 <= r1) or (l2 <= l1 <= r2 and l2 <= r1 <= r2):
        fully_enclosed += 1
    if (l1 <= l2 <= r1 or l1 <= r2 <= r1) or (l2 <= l1 <= r2 or l2 <= r1 <= r2):
        partially_enclosed += 1


print(f"Part 1 {fully_enclosed}\nPart 2 {partially_enclosed}")
