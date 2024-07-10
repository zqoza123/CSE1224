# Partner is Shachi Mahajan

#1
def oddOr8(li):
  result = []
  for x in li:
    if (x % 8 == 0 or x % 2 != 0):
      result.append(x)
  return result

#2
def whileLoop(li):
  result = []
  temp = 3
  while (temp < len(li) - 2):
    result.append(li[temp])
    temp+=2
  return result

#3
def mode(li):
  result = {}
  for number in li:
    if number in result:
      result[number] +=1
    else:
      result[number] =1 
  
  max = 0  
  mode = 0  

  for number, count in result.items():
    if count > max:
      max = count
      mode = number
      
  return mode

#4
def zee(n):
    

  result = [[0] * n for _ in range(n)]
    
  for x in range(n):
    result[0][x] = x + 1
        
  value = n + 1
  for i in range(1, n-1):
    result[i][n-i-1] = value
    value += 1
        
  for x in range(n):
    result[n-1][x] = value
    value += 1
        
  return result

print(zee(4))

#5
def triple(li):
  result = []
  for x in li:
    if (x <= 30 and x >= 10):
      result.append(x*3)
  return result

#6 
def prime(n):
  if (n > 1):
    for x in range (2, n):
      if (n % x) == 0:
        return False
  return True

def singlePrime(di):
  result = {}
  for keys, value in di.items():
    if (prime(keys) and not prime(value)) or (not prime(keys) and prime(value)):
      result[keys] = value
  return result
