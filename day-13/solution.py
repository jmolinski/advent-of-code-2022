from __future__ import annotations

with open("input.txt") as f:
    pairs = [[eval(v) for v in p.strip().split()] for p in f.read().split("\n\n")]
    all_packets = [x for p in pairs for x in p]


def cmp(l: list | int, r: list | int) -> int:
    if isinstance(l, int) and isinstance(r, int):
        return l - r
    elif isinstance(l, list) and isinstance(r, list):
        for i in range(min(len(l), len(r))):
            c = cmp(l[i], r[i])
            if c != 0:
                return c
        return len(l) - len(r)
    elif isinstance(l, int):
        return cmp([l], r)
    elif isinstance(r, int):
        return cmp(l, [r])
    else:
        raise Exception("Invalid input")


div1, div2 = [[2]], [[6]]
all_packets += [div1, div2]


def qsort(packets):
    if len(packets) <= 1:
        return packets
    pivot = packets[0]
    left = qsort([p for p in packets[1:] if cmp(p, pivot) < 0])
    right = qsort([p for p in packets[1:] if cmp(p, pivot) >= 0])
    return left + [pivot] + right


sorted_packets = qsort(all_packets)


print("Part 1:", sum(idx for idx, p in enumerate(pairs, start=1) if cmp(*p) < 0))
print("Part 2:", (sorted_packets.index(div1) + 1) * (sorted_packets.index(div2) + 1))
