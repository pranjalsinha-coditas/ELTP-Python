import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} ran in {end-start} time")
        return result
    return wrapper


@timer 
def example_function(n):
    time.sleep(n)

example_function(2)

def debug(func):
    def wrapper(*args, **kwargs):
        args_value = ', '.join(str(arg) for arg in args)
        kwargs_value = ', '.join(f"{k} = {v}" for k, v, in kwargs.items())
        print(f"calling: {func.__name__} with args {args_value}")
        result = func(*args, **kwargs)
        return result
    return wrapper

@debug
def hello():
    print("Hello")

@debug
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}")

hello()
greet("chai", greeting="hanji")

