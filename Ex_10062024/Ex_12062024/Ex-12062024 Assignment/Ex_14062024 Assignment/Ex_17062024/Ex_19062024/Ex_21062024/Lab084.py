def log_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"calling {func.__name__} with {args} and {kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__}")
        return result

    return wrapper()


@log_decorator
def add(a, b):
    return (a + b)
add (2,3)


