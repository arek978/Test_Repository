from contants import *
def range_generator(n):
    return list(range(n))

def fib_generator(n):
    if n < 2:   
        return n
    else:
        return n * fib_generator(n - 1)

def sum(a, b):
    return a + b

def div(a, b):
    return a - b

print(range_generator(5))
print(fib_generator(5))
print(sum(a,b))
print(div(a, b))
