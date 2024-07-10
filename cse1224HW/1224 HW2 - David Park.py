# 1. 
def numNegatives(li):
    count = 0
    for x in li:
        if x < 0:
            count += 1
    return count

# 2.
def multiFour(li):
    count = 0
    for x in li:
        if x % 4 == 0:
            count += 1
    return count

# 3.
def longestString(li):
    final = 0
    for x in li:
        if len(x) > final:
            final = len(x)
    return final

#4
def secondLargest(li):
  a, b = li[0], li[1]
    
  if a < b:
    a, b = b, a
  for n in li[2:]:
    if n > a:
      b = a
      a = n
    elif n > b:
      b = n
            
  return b
#5
def allOdd(li):
  for x in li:
    if x % 2 == 0:
      return False
  return True