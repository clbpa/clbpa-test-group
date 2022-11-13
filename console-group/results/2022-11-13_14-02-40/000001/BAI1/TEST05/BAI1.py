def gdc(x, y):
  if y == 0:
    return x
  return gdc(y, x % y)


def lcm(x, y):
  return int((x * y) / gdc(x, y))


a , b = [int(x) for x in input().split()]

print("{} {}".format(gdc(a, b), lcm(a, b)))
