# Write a decorator `arg_rules` that validates arguments passed to the function.
# A decorator should take 3 arguments:
# max_length: 15
# type_: str
# contains: [] - list of symbols that an argument should contain
# If some of the rules' checks returns False,
# the function should return False and print the reason it failed; otherwise, return the result.
# ```
#
#
# def arg_rules(type_: type, max_length: int, contains: list):
#     pass
#
#
# @arg_rules(type_=str, max_length=15, contains=['05', '@'])
# def create_slogan(name: str) -> str:
#     return f"{name} drinks pepsi in his brand new BMW!"
#
#
# assert create_slogan('johndoe05@gmail.com') is False
#
# assert create_slogan('S@SH05') == 'S@SH05 drinks pepsi in his brand new BMW!'
#
# ```
# Напишіть декоратор `arg_rules`, який перевіряє аргументи, передані функції.
# Декоратор повинен прийняти 3 аргументи:
# максимальна_довжина: 15
# тип_: вул
# містить: [] - список символів, які має містити аргумент
# Якщо деякі перевірки правил повертають False, функція повинна повернути False і вивести причину невдачі; інакше поверніть результат.
# ```
# def arg_rules(type_: тип, max_length: int, містить: список):
#      пройти
#
# @arg_rules(type_=str, max_length=15, містить=['05', '@'])
#
# def create_slogan(name: str) -> str:
#
#      return f"{name} п'є пепсі у своєму новому BMW!"
#
# assert create_slogan('johndoe05@gmail.com') є False
#
# assert create_slogan('S@SH05') == 'S@SH05 п'є пепсі у своєму новому BMW!'
#
# ```

def arg_rules(type_: type, max_length: int, contains: list):
    def decorator(func):
        def wrapper(name):
            if type(type_) != str:
                return False
            if max_length < 15:
                return False
            for i in contains:
                if i not in name:
                    return False
            rez = func(name)
            return rez

        return wrapper

    return decorator


@arg_rules(type_=str, max_length=15, contains=['05', '@'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"


assert create_slogan('johndoe05@gmail.com') is False

assert create_slogan('S@SH05') == 'S@SH05 drinks pepsi in his brand new BMW!'
