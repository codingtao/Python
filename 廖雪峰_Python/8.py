# 高级特性

# 切片
L = ['Michael','Sarsh','Tracy','Bob','Jack']

print('L[0:3] = ',L[0:3])
print('L[:3] = ',L[:3])
print('L[-2:] = ',L[-2:])

R = list(range(100))
print('R[:10] = ',R[:10])
print('R[:10:2] = ',R[:10:2])
print('R[::-1] = ',R[::-1])

# 迭代
# 利用for...in,,, 来作用于可迭代对象
# 通过collections模块中的Iterable类型判断是否为可迭代对象
from collections import Iterable,Iterator

def g():
    yield 1
    yield 2
    yield 3

print('Iterable? [1, 2, 3]:', isinstance([1, 2, 3], Iterable))
print('Iterable? \'abc\':', isinstance('abc', Iterable))
print('Iterable? 123:', isinstance(123, Iterable))
print('Iterable? g():', isinstance(g(), Iterable))

print('Iterator? [1, 2, 3]:', isinstance([1, 2, 3], Iterator))
print('Iterator? iter([1, 2, 3]):', isinstance(iter([1, 2, 3]), Iterator))
print('Iterator? \'abc\':', isinstance('abc', Iterator))
print('Iterator? 123:', isinstance(123, Iterator))
print('Iterator? g():', isinstance(g(), Iterator))

# iter list:
print('for x in [1, 2, 3, 4, 5]:')
for x in [1, 2, 3, 4, 5]:
    print(x)

print('for x in iter([1, 2, 3, 4, 5]):')
for x in iter([1, 2, 3, 4, 5]):
    print(x)

print('next():')
it = iter([1, 2, 3, 4, 5])
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))

d = {'a': 1, 'b': 2, 'c': 3}
# iter each key:
print('iter key:', d)
for k in d.keys():
    print('key:', k)

# iter each value:
print('iter value:', d)
for v in d.values():
    print('value:', v)

# iter both key and value:
print('iter item:', d)
for k, v in d.items():
    print('item:', k, v)

# iter list with index:
print('iter enumerate([\'A\', \'B\', \'C\']')
for i, value in enumerate(['A', 'B', 'C']):
    print(i, value)

# iter complex list:
print('iter [(1, 1), (2, 4), (3, 9)]:')
for x, y in [(1, 1), (2, 4), (3, 9)]:
    print(x, y)

# 列表生成式
L = [x*x for x in range(1,11) if (x%2==0)]
print(L)
L = [m+n for m in 'ABC' for n in 'XYZ']
print(L)

# practice 
# 列出当前目录下的所有文件和目录名
import os
L = [d for d in os.listdir()]
print(L)
# 把一个list所有字母变成小写
L = ['Hello','SAJDIS',18]
lower_L = [l1.lower() for l1 in L if isinstance(l1,str)]
print(lower_L)

# 生成器
# 一个函数中，如果包含yield，则这个函数就是一个生成器
def fib(max):
    n,a,b = 0,0,1
    while n < max:
        yield(b)
        a,b = b,a+b
        n = n + 1
    return 'done'

# generator 和函数的执行流程不一样
# 函数是遇到return 语句或者 最后一条语句返回
# 变成generator的函数，在每次调用next()的时候执行，在调用yield()语句返回，再次执行，从上次返回的yield语句处继续执行
g = fib(6)
while True:
    try:
        x = next(g)
        print('g:',x)
    except StopIteration as e:
        print('Generator return value:',e.value)
        break

# pectice 杨辉三角
def triangles():
    L = [1]
    while True:
        yield(L)
        L1 = L
        L = [L1[i]+L1[i+1] for i in range(len(L1)-1)]
        L.insert(0,1)
        L.append(1)

n = 0
for t in triangles():
    print(t)
    n = n + 1
    if n == 10:
        break
