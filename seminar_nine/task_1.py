from functools import wraps

def how_are_you(func):
    @wraps(func)
    def wrapper(arg):
        qst = input('How are you?:  ')
        msg = f'and I am chrenovo here is your {func.__name__}'
        if qst:
            print(msg)
        res = func(arg)
        return res
    return wrapper

@how_are_you
def factorial(n):
    f = 1
    for i in range(2, n + 1):
        f *= i
    return f

if __name__ == "__main__":
    print(f'{factorial(7) = }')



