with open("input.txt") as f:
    signals = f.read().strip()


def find_marker(length: int) -> int:
    for i in range(length - 1, len(signals)):
        if len(set(signals[i - length : i])) == length:
            return i


print(f"Part 1 {find_marker(4)}\nPart 2 {find_marker(14)}")
