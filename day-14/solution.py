from __future__ import annotations
from collections import defaultdict

with open("input.txt") as f:
    rocklines = []
    for l in f.readlines():
        turns = [tuple(map(int, t.split(","))) for t in l.split(" -> ")]
        rocklines.extend(list(zip(turns, turns[1:])))

    horizontal_rocklines, vertical_rocklines = defaultdict(list), defaultdict(list)
    rock_bottom = 0
    for (x1, y1), (x2, y2) in rocklines:
        rock_bottom = max(rock_bottom, y1, y2)
        if x1 == x2:
            horizontal_rocklines[x1].append((min(y1, y2), max(y1, y2)))
        else:
            vertical_rocklines[y1].append((min(x1, x2), max(x1, x2)))

    rock_bottom += 2


def is_blocked(point, sand_locations):
    if point in sand_locations:
        return True

    x, y = point
    for r in horizontal_rocklines[x]:
        if r[0] <= y <= r[1]:
            return True
    for r in vertical_rocklines[y]:
        if r[0] <= x <= r[1]:
            return True

    return False


def fall_one_step(
    particle_position: tuple[int, int], sand_locations: set[tuple[int, int]]
) -> tuple[int, int]:
    x, y = particle_position

    for new_x in (x, x - 1, x + 1):
        if not is_blocked((new_x, y + 1), sand_locations):
            return new_x, y + 1

    return particle_position


def spawn_new_sand_particle(
    sand_locations: set[tuple[int, int]]
) -> tuple[int, int] | None:
    particle_position = (500, 0)

    for _ in range(10_000):
        # if particle can't come to rest in 10_000 steps, it's falling forever
        new_particle_position = fall_one_step(particle_position, sand_locations)
        if new_particle_position == particle_position:
            return new_particle_position

        particle_position = new_particle_position

    return None


def run_simulation() -> int:
    sand_locations = set()

    while True:
        new_resting_sand_particle = spawn_new_sand_particle(sand_locations)
        if new_resting_sand_particle is None:  # particle couldn't come to rest
            break

        sand_locations.add(new_resting_sand_particle)

        if new_resting_sand_particle == (500, 0):
            break

    return len(sand_locations)


print("Part 1:", run_simulation())

original_is_blocked = is_blocked


def is_blocked(point, sand_locations):
    x, y = point
    if y >= rock_bottom:
        return True

    return original_is_blocked(point, sand_locations)


print("Part 2:", run_simulation())
