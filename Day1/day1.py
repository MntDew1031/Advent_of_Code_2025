def compute_password(rotations: str) -> int:
  """
  rotations: multiline string, each line like 'R29' or 'L68'
  returns: number of times the dial is at 0 after a rotation
  """
  pos = 50          # starting position
  zero_count = 0

  for line in rotations.splitlines():
      line = line.strip()
      if not line:
          continue  # skip empty lines if any

      direction = line[0]
      distance = int(line[1:])

      if direction == 'R':
          pos = (pos + distance) % 100
      elif direction == 'L':
          pos = (pos - distance) % 100
      else:
          raise ValueError(f"Invalid direction in line: {line}")

      if pos == 0:
          zero_count += 1

  return zero_count


if __name__ == "__main__":
  import sys

  # Read entire stdin as the puzzle input
  puzzle_input = sys.stdin.read()

  password = compute_password(puzzle_input)
  print(password)
