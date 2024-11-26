from functools import wraps

def count_func_call(func):
    @wraps(func)
    def wrapper(arg):
        wrapper.count += 1
        res = func(arg)
        print(f'Function {func.__name__} has been called for {wrapper.count} time(s) ')
        return res
    wrapper.count = 0
    return wrapper


@count_func_call
def factorial(n):
    f = 1
    for i in range(2, n + 1):
        f *= i
    return f

if __name__ == "__main__":
    print(f'{factorial(6) = }')
    print(f'{factorial(7) = }')
    print(f'{factorial(3) = }')