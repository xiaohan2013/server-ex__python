# 1. configparser

try:
    # py3
    import configparser as Configparser
except:
    # py2
    import ConfigParser



# 2. thread
try:
    # py2
    import thread
except:
    # py3
    import _thread as thread


# 3. hashlib
#py2
m_1 = hashlib.md5("abcd")
m_2 = hashlib.md5(data.encode("utf8"))


# 4. start web server
#py2
python -m SimpleHTTPServer
#py3
python -m http.server

# 5. base64.b64encode
#py2
base64.b64encode(feed_back)
#py3
base64.b64encode(feed_back.encode('utf-8'))
#py2
base64.encodestring(feed_back)
#py3
base64.encodestring(feed_back.encode('utf-8'))


# 6. long类型
Py3.X去除了long类型，现在只有一种整型——int，但它的行为就像2.X版本的long 
# py2
>>> long(1468984980.116425)
1468984980L
#py3
>>> int(1468984980.116425)
1468984980

# 7. iterterms()
# 在python2中，同时提供iterxxxx和xxxx方法。比如iteritems, items. 在python3 中不出现iterxxx. 默认都是生成器。
# py2
>>> a = {'a':'jia','b':'luo'}
>>> dir(a)
['__class__', '__cmp__', '__contains__', '__delattr__', '__delitem__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'clear', 'copy', 'fromkeys', 'get', 'has_key', 'items', 'iteritems', 'iterkeys', 'itervalues', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values', 'viewitems', 'viewkeys', 'viewvalues']
>>> for i in a.iteritems():
...     print i
...
('a', 'jia')
('b', 'luo')

#py3
>>> a = {'a':'jia','b':'luo'}
>>> dir(a)
['__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']
>>> a.items()
dict_items([('a', 'jia'), ('b', 'luo')])
>>> for i in a.items():
...     print(i)
...
('a', 'jia')
('b', 'luo')

# 8. queue
try:
    from Queue import PriorityQueue # py2
except:
    from queue import PriorityQueue # py3

# 9. raise
# py2
try:
    del self[key]
except KeyError, k:
    raise AttributeError, k

# py3
try:
    del self[key]
except KeyError as k:
    raise AttributeError(k)

# 10. exceptions
# py2
>>> from exceptions import UnicodeEncodeError
# py3
移除了 exceptions模块。

# 11. reload
# py2
import sys
from imp import reload
reload(sys)
# py3
import sys
from imp import reload
reload(sys)


# 12. sys.setdefaultencoding("utf-8")
# py2
import sys
sys.setdefaultencoding("utf-8")
# py3
取消了setdefaultencoding()



# 13. urllib&urllib2
#py2
>>> import urllib
>>> urllib.urlencode({'a':'jia','b':'xiao','c':'lei'})
'c=lei&a=jia&b=xiao'

#py3
>>> import urllib
>>> urllib.parse.urlencode({'a':'jia','b':'xiao','c':'lei'})
'c=lei&a=jia&b=xiao'

#py2
import urllib2
request = urllib2.Request(url)
opener = urllib2.urlopen(request)
except urllib2.HTTPError as msg:
except urllib2.URLError as msg:
# python2 中的urllib2， 在Python3中已经并入urllib.

#py3
import urllib.request
request = urllib.request.Request(url)
opener = urllib.request.urlopen(request)
except urllib.error.HTTPError as msg:
except urllib.error.URLError as msg:

# 14.url
try:
    from urlparse import urlparse # py2
except:
    from urllib.parse import urlparse # py3

# 15.DES
# py2
from des import DES