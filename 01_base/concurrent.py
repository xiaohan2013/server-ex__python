# -*- utf-8 -*-
#! /usr/bin/python

def consumer():
    r = ''
    while 1:
        n = yield r
        if not n:
            break

        print("consumer receive msg: %s" % n)
        r = "%s OK" % n

def produce():
    c = consumer()
    c.send(None)

    n = 0
    while n < 3:
        n += 1
        print('produce send msg: %s' % n)
        r = c.send(n)
        print('consumer return msg: %s' % r)
    c.close()

produce()