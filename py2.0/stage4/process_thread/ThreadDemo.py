from threading import Thread

def testThread(i):
    print('this is Thread',i)


def main():
    for i in range(0,3):
        # threads = Thread(target=testThread(i))
        #等价于：
        threads = Thread(target=testThread, args=(i,))
        threads.start()

if __name__ == '__main__':
    main()