"""
注意函数实参的调用方式 test(1, 2, 3, 4, a=1, b=2,c=3)
"""
def test(arg, *args, **kwargs):
    total = 0
    total =total+ arg
    for i in args:
        total = total+i

    print(f"arg={arg}, args={args}, kwargs={kwargs}")
    print(type(arg),type(args),type(kwargs),"\n")
    return total


test(1, 2, 3, 4, a=1, b=2,c=3)  # 1 (2, 3, 4) {'a': 1, 'b': 2, 'c': 3}
test(1, 2, 3, 4 )  # 1 (2, 3, 4) {}
print(test(1, 2, 3, 4))

