
def range_generator(n):
    return list(range(n))

def fib_generator(n):
    if n < 2:   
        return n
    else:
        return n * fib_generator(n - 1)

print(range_generator(5))
print(fib_generator(5))