def parse_rotations(rotations: str):
    """
    Parse lines like:
        R29
        L68
    into a list of (direction, steps) tuples.
    """
    result = []
    for line in rotations.splitlines():
        line = line.strip()
        if not line:
            continue
        direction = line[0]
        steps = int(line[1:])
        result.append((direction, steps))
    return result


def count_zeros_per_click(rotations: str) -> int:
    """
    Count how many times the dial points at 0 on ANY click
    (including during rotations), starting from 50.
    """
    pos = 50
    zero_count = 0

    for direction, steps in parse_rotations(rotations):
        delta = 1 if direction == 'R' else -1
        for _ in range(steps):
            pos = (pos + delta) % 100
            if pos == 0:
                zero_count += 1

    return zero_count


if __name__ == "__main__":
    import sys

    # Read puzzle input from stdin (same way as Part 1)
    puzzle_input = sys.stdin.read()
    answer = count_zeros_per_click(puzzle_input)
    print(answer)
