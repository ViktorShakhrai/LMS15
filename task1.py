# Write a decorator that prints a function with arguments passed to it.
# NOTE! It should print the function, not the result of its execution!
#
# For
# example:
#
# "add called with 4, 5"
#
# ```
#
#
# def logger(func):
#     pass
#
#
# @logger
# def add(x, y):
#     return x + y
#
#
# @logger
# def square_all(*args):
#     return [arg ** 2 for arg in args]
import datetime
import time
from functools import wraps


def decorator_info(func):
    @wraps(func)
    def wrapper(*args):
        func()
        print(f"{func.__name__} called with {args}")

    return wrapper()


@decorator_info
def add(arg_1, arg_2):
    return arg_1 + arg_2


add(1, 1)


def cache(func):
    my_dict = {}
    TTL = 5

    @wraps(func)
    def wrapper(*args, **kwargs):
        strok = (f"Decorate:{func.__name__} with parametrs: {args}{kwargs}")
        for i in my_dict:
            if (datetime.datetime.now() - my_dict[i][1]).seconds > TTL:
                my_dict.pop(i)
        if strok in my_dict:
            if (datetime.datetime.now() - my_dict[strok][1]).seconds < TTL:
                return my_dict[strok][0]
        my_dict[strok] = (func(*args, **kwargs), datetime.datetime.now())
        return my_dict[strok]

    return wrapper


@cache
def f1(num):
    print("Calculate")
    time.sleep(0.5)
    return num * 2


while True:
    z = input("Eneter: ")
    print(f1(int(z)))
