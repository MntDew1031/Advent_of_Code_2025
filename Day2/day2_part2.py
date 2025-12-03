def is_invalid_id_v2(n: int) -> bool:
    """
    Part 2 rule:
    An ID is invalid if its decimal representation is some sequence
    of digits repeated at least twice (2 or more times).
    """
    s = str(n)
    L = len(s)

    # Pattern length k must be < L and divide L
    # Also implies at least L/k >= 2 repeats
    for k in range(1, L // 2 + 1):
        if L % k != 0:
            continue
        repeats = L // k
        if repeats < 2:
            continue
        pattern = s[:k]
        if pattern * repeats == s:
            return True

    return False


def parse_ranges(line: str):
    """
    Parse comma-separated ranges like '11-22,95-115,...'
    into a list of (start, end) integer tuples.
    """
    ranges = []
    for part in line.split(","):
        part = part.strip()
        if not part:
            continue
        lo_str, hi_str = part.split("-")
        lo = int(lo_str)
        hi = int(hi_str)
        ranges.append((lo, hi))
    return ranges


def sum_invalid_ids_v2(ranges) -> int:
    total = 0
    for lo, hi in ranges:
        for n in range(lo, hi + 1):
            if is_invalid_id_v2(n):
                total += n
    return total


if __name__ == "__main__":
    import sys

    # Read the whole puzzle input (one long line) from stdin
    puzzle_input = sys.stdin.read().strip()
    ranges = parse_ranges(puzzle_input)
    answer = sum_invalid_ids_v2(ranges)
    print(answer)