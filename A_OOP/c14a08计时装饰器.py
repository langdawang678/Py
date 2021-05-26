import time


def wrapper(func):

    def fun(*args, **kwargs):
        print("....fun")
        start_time = time.time()

        func(*args, **kwargs)

        cost_time = time.time() - start_time
        print(cost_time)
        print(format(cost_time, '.2f'))

    return fun


@wrapper
def calc(a, b):
    print(a**b)

calc(10000, 10000)
