

def cache_deco(func):
    _cache_dict = {}
    def wrapper(arg):
        if not arg in _cache_dict:
            res = func(arg)
            _cache_dict[arg] = func(arg)
            return res
    return wrapper


@cache_deco
def factorial(n):
    f = 1
    for i in range(2, n + 1):
        f *= i
    return f

if __name__ == "__main__":
    print(f'{factorial(6) = }')
    print(f'{factorial(7) = }')
    print(f'{factorial(6) = }')
    print(f'{factorial(5) = }')
    print(f'{factorial(7) = }')
    print(f'{factorial(6) = }')