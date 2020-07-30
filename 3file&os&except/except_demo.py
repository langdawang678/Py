try:
    print("try可能错误的程序")
    raise ImportError
except:
    # pycharm提示"Too broad exception clause",
    # 因为捕获的异常过于宽泛，没有针对性，可以通过指定精确的异常类型来解决
    print("catch了exception，则else不执行")
    # 异常可以嵌套
    try:
        1 / 0
    except ZeroDivisionError:  # 这里的except不会提示波浪线，因为精确了异常类型
        print("1不能除以0，发生异常：ZeroDivisionError")
    except (TypeError, ZeroDivisionError, IOError):
        print("可以指定多个异常类型，相同操作的也可放在同一行")
else:
    print("当前没有异常，else执行（else和except只执行1个）")
finally:
    print("finally一直都会被执行")
    # finally关文件
