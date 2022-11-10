"""
 * Tìm ước số chung lớn nhất (USCLN)
 *
 * @param a: số nguyên dương
 * @param b: số nguyên dương
 * @return USCLN của a và b
"""
def uscln(a, b):
  if (b == 0):
    return a
  return uscln(b, a % b)
 
"""
 * Tìm bội số chung nhỏ nhất (BSCNN)
 * 
 * @param a: số nguyên dương
 * @param b: số nguyên dương
 * @return BSCNN của a và b
"""
def bscnn(a, b):
  return int((a * b) / uscln(a, b))
 


with open("BAI-1.IN", "r") as inp:
  parts = inp.read().split()

a = int(parts[0])
b = int(parts[1])

with open("BAI-1.OUT", "w") as out:
  out.write("{} {}".format(uscln(a, b), bscnn(a, b)))
