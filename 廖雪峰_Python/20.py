#进程 和 线程
# import os

# print('Process (%s) start...' % os.getpid())

# pid = os.fork()
# if pid == 0:
#     print('I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid()))
# else:
#     print('I (%s) just created a child process (%s).' % (os.getpid(), pid))

# 由于任何进程默认启动一个线程，我们把该线程称为主线程，主线程又可以启动新的线程
# current_thread(): Python 的threading模块有个current_thread()函数,它永远返回当前线程的实例
# 主线程实例的名字为：MainThread ; 子线程的名字在创建的时候指定，我们用LoopThread命名子线程
# 线程参考： http://www.jianshu.com/p/0e4ff7c856d3
# start():
# join():线程运行sleep()或join()方法后，线程进入Sleeping状态。区别在于sleep等待固定的时间，而join是等待子线程执行完。

# import time, threading

# # 新线程执行的代码:
# def loop():
#     print('thread %s is running...' % threading.current_thread().name)
#     n = 0
#     while n < 5:
#         n = n + 1
#         print('thread %s >>> %s' % (threading.current_thread().name, n))
#         time.sleep(1)
#     print('thread %s ended.' % threading.current_thread().name)

# print('thread %s is running...' % threading.current_thread().name)
# t = threading.Thread(target=loop, name='LoopThread')
# t.start()
# t.join()
# print('thread %s ended.' % threading.current_thread().name)

import time,threading

balance = 0
lock = threading.Lock()

def change_it(n):
    # 先存后取，结果为0
    global balance
    balance = balance + n
    balance = balance - n

def run_thread(n):
    for i in range(1000000):
        # 先获取锁
        lock.acquire()
        try:
            change_it(n)
        finally:
            # 释放锁
            lock.release()

t1 = threading.Thread(target = run_thread,args = (5,))
t2 = threading.Thread(target = run_thread,args = (8,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)