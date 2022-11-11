def gdc(x, y):
  if y == 0:
    return x
  return gdc(y, x % y)


def lcm(x, y):
  return int((x * y) / gdc(x, y))


with open("BAI-1.IN", "r") as inp:
  parts = inp.read().split()

a = int(parts[0])
b = int(parts[1])

with open("BAI-1.OUT", "w") as out:
  out.write("{} {}".format(gdc(a, b), lcm(a, b)))
