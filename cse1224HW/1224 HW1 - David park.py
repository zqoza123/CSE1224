# 1. 
def greaterThan10 (num):
    return num > 10

# 2. the type of value that is returned is an boolean value.

# 3.
def fahrToCel(n):
    return (n-32) * (5/9)
    
# 4.
def celcToFahr(n):
    return (n * (9/5)) + 32

# 5. The value returned is just N as itself.

# 6.
def harmonic(n):
    final = 0
    x = 1
    while x <= n:
        final += 1/x
        x+=1
    return final
    
