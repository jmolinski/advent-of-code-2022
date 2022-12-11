with open("input.txt") as f:
    forest = [[int(c) for c in l.strip()] for l in f.readlines()]


LEFT, RIGHT, UP, DOWN = 1, 2, 4, 8
VECTOR = {
    LEFT: (0, 1),
    RIGHT: (0, -1),
    UP: (1, 0),
    DOWN: (-1, 0),
}


def is_first_in_sight_line(y: int, x: int, direction: int) -> bool:
    if y == 0 and direction == UP:
        return True
    if y == len(forest) - 1 and direction == DOWN:
        return True
    if x == 0 and direction == LEFT:
        return True
    if x == len(forest[0]) - 1 and direction == RIGHT:
        return True

    return False


def is_visible_from_direction(y: int, x: int, direction: int) -> bool:
    if is_first_in_sight_line(y, x, direction):
        return True

    rightmost_x = len(forest[0]) - 1
    bottommost_y = len(forest) - 1

    to = (y, x)
    from_ = {
        UP: (0, x),
        DOWN: (bottommost_y, x),
        LEFT: (y, 0),
        RIGHT: (y, rightmost_x),
    }[direction]
    dy, dx = VECTOR[direction]

    max_seen = -1
    current_y, current_x = from_
    while to != (current_y, current_x):
        current_tree_height = forest[current_y][current_x]

        if current_tree_height > max_seen:
            max_seen = current_tree_height

        current_y += dy
        current_x += dx

    return max_seen < forest[y][x]


def is_visible(y: int, x: int) -> bool:
    for direction in VECTOR:
        if is_visible_from_direction(y, x, direction):
            return True

    return False


def scenic_score_to_direction(y: int, x: int, direction: int) -> int:
    dy, dx = VECTOR[direction]

    center_height = forest[y][x]
    visible_trees = 0
    current_y, current_x = y - dy, x - dx

    while True:
        visible_trees += 1

        if forest[current_y][current_x] >= center_height:
            break
        if is_first_in_sight_line(current_y, current_x, direction):
            break

        current_y -= dy
        current_x -= dx

    return visible_trees


def get_scenic_score(y: int, x: int) -> int:
    if any(is_first_in_sight_line(y, x, d) for d in [LEFT, RIGHT, UP, DOWN]):
        return 0

    score = 1
    for direction in VECTOR:
        score *= scenic_score_to_direction(y, x, direction)

    return score


visible_count = 0
max_scenic_score = 0
for y in range(len(forest)):
    for x in range(len(forest[0])):
        if is_visible(y, x):
            visible_count += 1

        if not (x == 0 or x == len(forest[0]) - 1 or y == 0 or y == len(forest) - 1):
            max_scenic_score = max(max_scenic_score, get_scenic_score(y, x))


print("Part 1:", visible_count)
print("Part 2:", max_scenic_score)
