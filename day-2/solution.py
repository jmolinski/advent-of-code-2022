with open("input.txt") as f:
    elfs = [tuple(e.strip().split()) for e in f.readlines()]


sign_score = {
    'rock': 1,
    'paper': 2,
    'scissors': 3,
}

fst_column_to_sign = {
    'A': 'rock',
    'B': 'paper',
    'C': 'scissors',
}

snd_column_to_sign = {
    'X': 'rock',
    'Y': 'paper',
    'Z': 'scissors',
}

snd_column_to_result = {
    'X': 0,
    'Y': 3,
    'Z': 6,
}

key_beats_value = {
    'rock': 'scissors',
    'paper': 'rock',
    'scissors': 'paper',
}

value_beats_key = dict((v, k) for k, v in key_beats_value.items())

def part1(data: list[tuple[str, str]]) -> int:
    score = 0
    for (fst, snd) in data:
        fst_sign = fst_column_to_sign[fst]
        snd_sign = snd_column_to_sign[snd]

        score += sign_score[snd_sign]

        if fst_sign == snd_sign:
            score += 3
        elif key_beats_value[snd_sign] == fst_sign:
            score += 6

    return score


def part2(data: list[tuple[str, str]]) -> int:
    score = 0
    for (fst, snd) in data:
        fst_sign = fst_column_to_sign[fst]
        result_score = snd_column_to_result[snd]

        score += result_score

        if result_score == 0:
            snd_sign = key_beats_value[fst_sign]
        elif result_score == 3:
            snd_sign = fst_sign
        else:
            snd_sign = value_beats_key[fst_sign]

        score += sign_score[snd_sign]

    return score


print("Part 1", part1(elfs))
print("Part 2", part2(elfs))
