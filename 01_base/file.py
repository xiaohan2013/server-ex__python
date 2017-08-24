# -*- utf-8 -*-
#!/usr/bin/python

try:
    f = open('generator.py', 'r', encoding='UTF-8')
    print(f.read())
    # f.close()
finally:
    if f:
        f.close()


'''
    简化上述写法
'''
with open('generator.py', 'r', encoding='UTF-8') as f:
    print(f.read())


'''
    StringIO, BytesIO

    StringIO: 字符串IO
    - 先从io中引入StringIO
    - 创建一个stringIO对象
    - 写字符串到StringIO对象f中
    - 获取字符串内容： f.getvalue()

'''

from io import StringIO, BytesIO
f = StringIO()
f.write('hello')
print(f.getvalue())