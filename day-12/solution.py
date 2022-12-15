from collections import defaultdict

with open("input.txt") as f:
    maze = [l.strip() for l in f.read().splitlines()]

for i, line in enumerate(maze):
    if "S" in line:
        START = (i, line.index("S"))
        maze[i] = line.replace("S", "a")
    if "E" in line:
        END = (i, line.index("E"))
        maze[i] = maze[i].replace("E", "z")

assert START and END

maze = [[ord(c) - ord("a") for c in l] for l in maze]

graph: defaultdict[tuple[int, int], list[tuple[int, int]]] = defaultdict(list)
for y in range(len(maze)):
    for x in range(len(maze[0])):
        center = maze[y][x]
        if y > 0 and maze[y - 1][x] - center <= 1:
            graph[(y, x)].append((y - 1, x))
        if y < len(maze) - 1 and maze[y + 1][x] - center <= 1:
            graph[(y, x)].append((y + 1, x))
        if x > 0 and maze[y][x - 1] - center <= 1:
            graph[(y, x)].append((y, x - 1))
        if x < len(maze[y]) - 1 and maze[y][x + 1] - center <= 1:
            graph[(y, x)].append((y, x + 1))


def bfs_search(graph, start, goal) -> int:
    visited = set()

    if start == goal:
        return 0

    queue = [[start]]

    while queue:
        path = queue.pop(0)
        node = path[-1]

        if node in visited:
            continue
        visited.add(node)

        for neighbor in graph[node]:
            new_path = path + [neighbor]

            if neighbor == goal:
                return len(new_path)

            queue.append(new_path)

    return -1


print("Part 1:", bfs_search(graph, START, END) - 1)

starting_points = [
    (y, x) for y in range(len(maze)) for x in range(len(maze[0])) if maze[y][x] == 0
]
print(
    "Part 2:",
    min(
        path_length
        for start in starting_points
        if (path_length := bfs_search(graph, start, END)) != -1
    )
    - 1,
)
