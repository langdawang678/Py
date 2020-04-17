# encoding=utf-8
from multiprocessing import Process


def test(i):
    print('this is process',i)


def main():
    for i in range(0, 3):
        print("main start")
        p = Process(target=test, args=(i,))
        p.start()
        print("main end")


if __name__ == '__main__':
    main()
'''
其他多线程方式 os.fork()，或者multiprocessing的Pool类
'''