def compress(uncompressed):
  result = ""
  k = 1
  uncompressed = uncompressed + " "
  for i in range(0, len(uncompressed) - 1):
    if uncompressed[i] == uncompressed[i + 1]:
      k += 1
    else:
      if k > 1:
        result = result + str(k)
      result = result + uncompressed[i]
      k = 1
  return result


with open("BAI-3.IN", "r") as inp:
  s = str(inp.read())

with open("BAI-3.OUT", "w") as out:
  out.write(compress(s))
