#-*- utf-8 -*- 
#!/usr/bin/python


'''

    Python的进程管理

'''

import os, sys

# os.fork()无法在windows上运行。
# pid = os.fork()

# if pid == 0:
#     print("%s %s" % (os.getpid(), os.getppid()))
# else:
#     print("%s %s" % (os.getpid(), pid))


import multiprocessing, time
def func(msg):
    for i in xrange(3):
        print(i)
        time.sleep(1)

if __name__ == "__main__":
    p = multiprocessing.Process(target = func, args=("hell", ))
    p.start()
    p.join()


