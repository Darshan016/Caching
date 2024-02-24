import time


def cache(func):
    cached_data = {}

    def wrapper(*args):
        if args in cached_data:
            return cached_data[args]
        result = func(*args)
        cached_data[args] = result
        return result

    return wrapper


@cache
def sum_of_two_numbers(a, b):
    time.sleep(5)
    return a + b


print(sum_of_two_numbers(2, 3))
print(sum_of_two_numbers(2, 3))
