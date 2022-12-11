from __future__ import annotations
from collections import deque


class Monke:
    def __init__(self, data: str) -> None:
        lines = list(map(str.strip, data.splitlines()))
        self.original_items = list(
            map(int, map(str.strip, lines[1].split(":")[1].split(",")))
        )
        self.items = deque(self.original_items.copy())

        operation = lines[2].split("=")[1].strip().replace(" ", "")
        left_operand, right_operand = [
            (lambda v: v) if op == "old" else (lambda _: int(op))
            for op in (
                operation.split("+") if "+" in operation else operation.split("*")
            )
        ]
        if "+" in operation:
            self.operation = lambda old: (left_operand(old) + right_operand(old))
        else:
            self.operation = lambda old: (left_operand(old) * right_operand(old))

        self.divisor = int(lines[3].split("by ")[1])
        self.test = lambda v: (v % self.divisor == 0)

        self.if_true = int(lines[4].split("monkey ")[1].strip())
        self.if_false = int(lines[5].split("monkey ")[1].strip())

        self.inspections = 0

    def run_inspections(self, peers: list[Monke], divide_level: bool) -> None:
        while self.items:
            it = self.items.popleft()
            it = self.operation(it)
            self.inspections += 1
            it %= global_divisor
            if divide_level:
                it //= 3
            if self.test(it):
                peers[self.if_true].items.append(it)
            else:
                peers[self.if_false].items.append(it)

    def reset(self) -> None:
        self.inspections = 0
        self.items = deque(self.original_items.copy())


with open("input.txt") as f:
    monkeys = list(map(Monke, f.read().split("\n\n")))
    global_divisor = 1
    for m in monkeys:
        global_divisor *= m.divisor


def run_simulation(rounds: int, divide_levels: bool) -> int:
    for m in monkeys:
        m.reset()

    for _ in range(rounds):
        for m in monkeys:
            m.run_inspections(monkeys, divide_levels)

    top_2, top_1 = sorted(m.inspections for m in monkeys)[-2:]
    return top_1 * top_2


print("Part 1:", run_simulation(20, True))
print("Part 2:", run_simulation(10000, False))
