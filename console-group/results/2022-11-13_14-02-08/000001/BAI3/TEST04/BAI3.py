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


s = str(input())
print(compress(s))
