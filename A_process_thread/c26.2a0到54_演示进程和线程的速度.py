# import os
# import time
# import threading
# from multiprocessing import Queue, Pool, Process, Manager
#
#
# def work():
#     print(f"{os.getpid()}")
#     time.sleep(1)
#
# # 1/多进程
# if __name__ == '__main__':
#
#     q3 = Manager().Queue()
#     for i in range(1000):
#         q3.put("127.0.0.1")
#
#     time1 = time.time()
#     pool = Pool(3)
#     for i in range(q3.qsize()):
#         pool.apply_async(work, args=(q3,))
#     pool.close()
#     pool.join()
#     time2 = time.time() - time1
#     print(time2)  # 0.6230158805847168
#
# # 2/多线程
# # if __name__ == '__main__':
# #     t1 = threading.Thread(target=work)
# #     t2 = threading.Thread(target=work)
# #     t3 = threading.Thread(target=work)
# #     time1 = time.time()
# #     t1.start()
# #     t2.start()
# #     t3.start()
# #     t1.join()
# #     t2.join()
# #     t3.join()
# #     time2 = time.time() - time1
# #     print(time2)  # 1
