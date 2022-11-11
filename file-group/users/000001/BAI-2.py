import math


def is_prime(num):
  if num < 2:
    return False
  if num < 4:
    return True
  if num % 2 == 0:
    return False
  for i in range(5, int(math.sqrt(num)) + 1, 2):
    if num % i == 0:
      return False
  return True


with open("BAI-2.IN", "r") as inp:
  n = int(inp.read())

with open("BAI-2.OUT", "w") as out:
  if is_prime(n):
    out.write("true")
  else:
    out.write("false")
