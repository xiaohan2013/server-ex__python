#  -*- utf-8 -*-
#!/usr/bin/python



def fab1(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1


def fab2(max):
    n, a, b = 0, 0, 1
    L = []
    while n < max:
        L.append(b)
        a, b = b, a + b
        n = n + 1
    return L


class Fab(object):

    def __init__(self, max):
        self.max = max
        self.n, self.a, self.b = 0, 0, 1

    def __iter__(self):
        '''
        迭代器对象
        '''
        return self

    def next(self):
        if self.n < self.max:
            r = self.b
            self.a, self.b = self.b, self.a + self.b
            self.n = self.n + 1
            return r
        raise StopIteration()



'''
生成器函数只有在调用__next__()方法时才开始执行函数里的语句
'''
def fab3(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1


'''
用yield生成模拟Linux中的: tail -f file | grep python

查找监控日志文件中的python


'''
import time
def tail(f):
    f.seek(0, 2)
    while True:
        line = f.readline()
        if not line:
            time.sleep(0.1)
            continue
        yield line


def grep(lines, searchText):
    for line in lines:
        if searchText in line:
            yield line




if __name__ == '__main__':
    result = fab1(5)
    f = fab3(23)
    # print(f.next())
    # print(f.send(None))
    # print(f.send(None))
    print(f.__next__())
    print(f.__next__())
    print(f.__next__())
    print(f.__next__())
    print(f.__next__())
    print(f.__next__())