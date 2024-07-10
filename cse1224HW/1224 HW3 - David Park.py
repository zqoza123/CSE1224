#1
def numbers(start, end, step):
    result = []
    counter = start
    while (counter <= end):
        result.append(counter)
        counter+= step
    return result
    
#2
def foo(n):
    result = 0
    i = 2
    while (i < n):
        j=3
        while(j < n+1):
            result += j
            j+=1
        i+=3
    return result
        
#3
def reverse(di):
  result = {}
  for temp1, temp2, in di.items():
    result[temp2] = temp1
  return result

#4 
def integerCount(li):
    counts = {}
    for num in li:
        if num in counts:
            counts[num]+=1
        else:
            counts[num]=1 
    return counts

#5
def antiDiagonal(n):
    result = []
    for x in range(n):
        result.append([0] * n)

    for row in range(n):
        column = n - row - 1
        result[row][column] = 1

    return result
    