def square(n):
    result = []
    if n <= 2:
        print("enter a number greater than 2")
        return None
    
    for _ in range (n):
        result.append([0] * n)
    
    for i in range (n):
        result[0][i] = 1
        result[n-1][i] = 1
        result[i][0] = 1
        result[i][n-1] = 1
    return result


def dictionaryToList(di):
    result = []
    for key, value in di.items():
        for i in range(value):
            result.append(key)
    result.sort()
    return result

