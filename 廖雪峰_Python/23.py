import struct
import hashlib
import itertools
from contextlib import contextmanager

bmp_header = b'\x42\x4d\x38\x8c\x0a\x00\x00\x00\x00\x00\x36\x00\x00\x00\x28\x00\x00\x00\x80\x02\x00\x00\x68\x01\x00\x00\x01\x00\x18\x00'

print(struct.unpack('<ccIIIIIIHH',bmp_header))

md5 = hashlib.md5()
md5.update('how to use hashlib in the python md5?'.encode('utf-8'))
print(md5.hexdigest())

natuals = itertools.count(1)
ns = itertools.takewhile(lambda x:x<10,natuals)
print(list(ns))

@contextmanager
def tag(name):
    print('<%s>' % name)
    yield
    print('</%s>' % name)

with tag('h1'):
    print('hello')
    print('world')