from time import sleep

def slow_down(digits):
    def deco(func):
        def wrapper(arg):
            sleep(digits)
            print(f'Function {func.__name__} slowed down for {digits} sec(s)')
            result = func(arg)
            return result
        return wrapper
    return deco

@slow_down(5)
def factorial(n):
    f = 1
    for i in range(2, n + 1):
        f *= i
    return f


if __name__ == "__main__":
    print(f'{factorial(7) = }')
