#函数式编程
# 高阶函数 

# 1 变量可以指向函数
f = abs;
print(f(-1))

# 2 函数名也是变量
# 函数名是指向函数的变量

# 3 一个函数可以接收变量 也就可以接收另一个函数作为参数

def add(x,y,f):
    return f(x) + f(y)

print(add(-1,2,abs))

# map 和　reduce
# 1 map  
# map(f函数,序列１，序列２，...) :　常见的序列有list tuple str
# 当函数为None时，操作和zip相似：
# 描述　f函数将作用于序列中的每一个元素，返回值是一个集合，可以用list(r)生成一个list

r = map(str,[1,2,3,4])
print(list(r))

def f1(x,y):
    return (x,y)
l1 = [1,2,3]
l2 = ['a','b','c']
print(list(map(f1,l1,l2)))


# 2 reduce
# reduce(f函数，[x1,x2,x3]序列)
# 描述　f函数作用在序列上的两个元素(即：f是一个有两个参数的函数)，reduce把结果继续和序列的下一个元素做累积计算
# f作用于序列的前两个元素，如果ｆ有初始化参数，则f作用于初始化参数和序列的第一个参数
# map的返回值可以当做reduce的序列参数
# 例如　reduce(f,[x1,x2,x3]) = f(f(x1,x2),x3)
from functools import reduce

def str2int(s):
    def fn(x,y):
        return x*10+y
    def char2num(s):
        return {'0':0,
                '1':1,
                '2':2,
                '3':3,
                '4':4,
                '5':5,
                '6':6,
                '7':7,
                '8':8,
                '9':9     
                }[s]
    return reduce(fn,map(char2num,s))

print(str2int('123'))

# practice
# 1
def normalize(name):
    return name[0].upper() + name[1:].lower()

L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)         

# 2
def prod(L):
    def f(x,y):
        return x * y  
    return reduce(f,L)

print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))   

# 3
def str2float(s):
    def char2num(s):
        return {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}[s]
    def f(x,y):
        return 10 * x + y
    n = s.index('.') 
    s1 = s[:n] + s[n+1:]
    x = reduce(f,map(char2num,s1))
    return x/10**(len(s)-n-1)

print('str2float(\'123.456\') =', str2float('123.456'))    

# 3 filter
# filter(f函数，序列)
# filter把函数ｆ作用于序列中的每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素
def is_odd(n):
    return n%2==1

print(list(filter(is_odd,[1,2,3,4,5])))

def not_empty(s):
    return s and s.strip()

print(list(filter(not_empty,['A','',None,'B',' '])))

# 用filter求素数　埃氏筛选法
# 1 先构造一个从3开始的奇数序列
def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n
# 2 定义一个筛选函数
def _not_division(n):
    return lambda x:x%n>0
# 3 定义一个生成器，不断返回下一个素数
def primes():
    yield 2
    it = _odd_iter() #初始序列
    while True:
        n = next(it) #返回序列的第一个数
        yield n 
        it = filter(_not_division(n),it) #构造新序列
# 4 打印10 以内的素数
for n in primes():
    if n < 10:
        print(n)
    else:
        break        

# practice
def is_palindrome(n):
    s1 = str(n)
    s2 = s1[::-1] # 字符串反转，以步长为-1操作
    return s1 == s2
output = filter(is_palindrome, range(1, 1000))
print(list(output))

# 4 sorted
# sorted(list)
# sorted(list,key=abs)
# sorted(list,key=str.lower,reverse = True)
# practice
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
def by_name(t):
    return t[0].lower()

def by_score(t):
    return t[1]
    
L2 = sorted(L, key=by_name)
print(L2)
L2 = sorted(L, key=by_score,reverse = True)
print(L2)