with open("input.txt") as f:
    instructions = [l.strip() for l in f.readlines()]

x = 1
historic_x_values = [x]
for i in instructions:
    historic_x_values.append(x)
    if i == "noop":
        pass
    else:
        historic_x_values.append(x)
        v = int(i.split(" ")[-1])
        x += v

signal_strengths = [i * v for i, v in enumerate(historic_x_values)]

print("Part 1:", sum(signal_strengths[20::40]))

print("Part 2:")

for r in range(len(historic_x_values) // 40):
    row = historic_x_values[r * 40 + 1 : (r + 1) * 40 + 1]
    for i, x_value in enumerate(row):
        if x_value - 1 <= i <= x_value + 1:
            print("##", end="")
        else:
            print("  ", end="")
    print()
