import functools

def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

@functools.cache
def fibonacci_cache(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci_cache(4))
print(fibonacci_cache(40))

print(fibonacci(4))
print(fibonacci(40))

