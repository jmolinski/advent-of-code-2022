with open("input.txt") as f:
    moves = [(p[0], int(p[1])) for l in f.readlines() if (p := l.strip().split(" "))]


VECTOR = {
    "U": (-1, 0),
    "D": (1, 0),
    "L": (0, -1),
    "R": (0, 1),
}


def move_tail(hy, hx, ty, tx) -> tuple[int, int]:
    dx, dy = abs(hx - tx), abs(hy - ty)
    if dx + dy < 2 or (dx == 1 and dy == 1):
        return ty, tx

    if dx == 1:
        tx = hx
    if dy == 1:
        ty = hy
    if dx == 2:
        tx = (tx + hx) // 2
    if dy == 2:
        ty = (ty + hy) // 2

    return ty, tx


def solve(knots_count: int) -> int:
    knots = [(0, 0) for _ in range(knots_count)]

    visited = {(0, 0)}
    for d, cnt in moves:
        dy, dx = VECTOR[d]
        for _ in range(cnt):
            hx, hy = knots[0]
            knots[0] = (hx + dx, hy + dy)

            for i in range(1, knots_count):
                knots[i] = move_tail(*knots[i - 1], *knots[i])

            visited.add(knots[-1])

    return len(visited)


print("Part 1:", solve(2))
print("Part 2:", solve(10))
