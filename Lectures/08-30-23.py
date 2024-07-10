def square(num): 
  result = num ** 2
  return result



def curveGrade(n, curve):
    
    
    
def sumOrMultiply(n, m) :
    if n % 2 = 0 and m % 2 = 0:
        return n + m
    else:
        return n * m
    
    
    
def absoluteValue(n):
    return (n * n) + n
    
    
def slope(x1, y1, x2, y2):
    return None if x1 == x2 else (y2-y1) / (x2-x1) 
    
    
def weeklyPay(hoursWorked, hourlyRate):
    if hoursWorked > 40:
        excessHours = hoursWorked - 40
        return (40 * hourlyRate) + excessHours * (hourlyRate * 1.5)
    else:
        return hoursWorked * hourlyRate
    
    

    
'''
HOMEWORK 09/07/23 DUE DATE
'''
def greaterThan10 (num):
    if num > 10:
        return True
    else:
        return False


def fahrToCel(n):
    return (n-32) * (5/9)
    

def celcToFahr(n):
    return (n * 2) + 32



def harmonic(n):
    
    
    
    
    
'''
Problems for 09/01/23
'''


def sumOdds(m, n):
    final = 0
    while m <= n:
        if m % 2 != 0:
            final += m
            m+= 1
        else:
            m+= 1
    return final
    
def isPrime(n):
    final = True
    x = 1
    while x <= n:
        if (n % x == 0):
            final = False
        x+=1
    return final


def numberOfPrimes(n):
  numPrimes = 0
  start = 2
  while start <= n:
    if isPrime(start):
      numPrimes += 1
    start += 1
  return numPrimes

    
def fibonacciNum (n):
    x = 0;
    firstNum = 0;
    secondNum = 1;
    while (x < n):
        
        