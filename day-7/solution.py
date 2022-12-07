from __future__ import annotations


class Dir:
    files: dict[str, int]
    dirs: dict[str, Dir]
    parent: Dir

    def __init__(self, parent: Dir) -> None:
        self.parent = parent
        self.dirs = {}
        self.files = {}

    def size(self) -> int:
        return sum(self.files.values()) + sum(d.size() for d in self.dirs.values())

    def innerdirs(self):
        for d in self.dirs.values():
            yield from d.innerdirs()
            yield d


with open("input.txt") as f:
    prompts = [
        [l.strip() for l in p.strip().split("\n")]
        for p in f.read().split("$ ")
        if p.strip()
    ]
    assert prompts[0] == ["cd /"]

wd = root = Dir(None)  # type: ignore

for [p, *out] in prompts:
    if p == "ls":
        for l in out:
            if l.startswith("dir "):
                dname = l.split(" ")[1]
                assert dname not in wd.dirs
                wd.dirs[dname] = Dir(wd)
            else:
                size, fname = l.split(" ")
                wd.files[fname] = int(size)
    else:
        assert out == []
        target = p.split(" ")[-1]
        if target == "..":
            wd = wd.parent
        elif target == "/":
            wd = root
        else:
            wd = wd.dirs[target]

device_size, required_mem = 70000000, 30000000
min_to_delete_size = required_mem - (device_size - root.size())

alldirs = [root] + list(root.innerdirs())

print("Part 1:", sum(d.size() for d in alldirs if d.size() <= 100000))
print("Part 2:", min(d.size() for d in alldirs if d.size() >= min_to_delete_size))
