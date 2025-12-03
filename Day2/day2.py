def is_invalid_id(n: int) -> bool:
  """
  Return True if n is made of some digit sequence repeated twice.
  Examples: 11, 6464, 123123, 1010.
  """
  s = str(n)
  # Must have even length
  if len(s) % 2 == 1:
      return False

  mid = len(s) // 2
  return s[:mid] == s[mid:]


def parse_ranges(line: str):
  """
  Parse a comma-separated list of ranges like:
    '11-22,95-115,...'
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


def sum_invalid_ids(ranges) -> int:
  total = 0
  for lo, hi in ranges:
      for n in range(lo, hi + 1):
          if is_invalid_id(n):
              total += n
  return total


if __name__ == "__main__":
  import sys

  # Read the whole input as a single string (one line)
  puzzle_input = sys.stdin.read().strip()
  ranges = parse_ranges(puzzle_input)
  answer = sum_invalid_ids(ranges)
  print(answer)
