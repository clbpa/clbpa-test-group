import math

def is_prime(n):
  if (n < 2):
    return False
  if (n < 4):
    return True
  if (n % 2 == 0):
    return False
  for i in range(5, int(math.sqrt(n))+1, 2):
    if (n % i == 0):
      return False
  return True

with open("BAI-2.IN", "r") as inp:
  n = int(inp.read())

with open("BAI-2.OUT", "w") as out:
  if (is_prime(n)):
    out.write("true")
  else:
    out.write("false")
