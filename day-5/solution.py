with open("input.txt") as f:
    board, moves = f.read().split("\n\n")
    moves = [
        [int(s) for s in move.split() if all(c in "1234567890" for c in s)]
        for move in moves.split("\n")
        if move.strip()
    ]

    board = [r[1::4] for r in board.split("\n")[:-1]][::-1]
    STACKS = [[] for _ in range(len(board[0]))]
    for r in board:
        for i, c in enumerate(r):
            if c.strip():
                STACKS[i].append(c)


def solve(part: int) -> str:
    stacks = [s[:] for s in STACKS]

    for quantity, source, target in moves:
        source, target = stacks[source - 1], stacks[target - 1]

        new_target_top = source[-quantity:]
        if part == 1:
            new_target_top = new_target_top[::-1]
        source[-quantity:], target[:] = [], target[:] + new_target_top

    return "".join(s.pop() for s in stacks)


print(f"Part 1 {solve(1)}\nPart 2 {solve(2)}")
