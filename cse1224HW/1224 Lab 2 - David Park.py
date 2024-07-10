def posOddNegEven(li):
  result = []
  for x in li:
    if x > 0 and x % 2 == 1:
        result.append(x)
    elif x < 0 and x % 2 == 0:
        result.append(x)
  return result

def posOddNegEvenCount(li):
    count = 0
    for x in li:
        if x > 0 and x % 2 == 1:
            count += 1
        elif x < 0 and x % 2 == 0:
            count += 1
    return count

li = [4, -2, -3, 6, 7, 10, 3]
print(posOddNegEven(li)) 

print(posOddNegEvenCount(li))
