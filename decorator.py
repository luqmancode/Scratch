import time

def time_it(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time() - start
        print(f"Function {func.__name__!r} took {end:.8f} time in seconds")
        return result
    return wrapper


@time_it
def print_name(name: str) -> None:
    print(f"Hi there!, My name is {name}")

print_name("MOhamed")