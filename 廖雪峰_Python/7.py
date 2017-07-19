# Python 函数

n1 = 255
n2 = 1000

# 内建函数
print(hex(n1))
print(hex(n2))

# 自定义函数 + 参数类型检查
def my_abs(x):
    if not isinstance(x,(int,float)):
        raise TypeError('bad operand type')
        
    if x < 0:
        return -x
    else:
        return x

print(my_abs(-11))

# 引入包，返回多个函数,返回值是一个tuple
import math

def move(x,y,step,angle = 0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx,ny

x,y = move(100,100,60,math.pi/6)
print(x,y)

# practice 

def quadratic(a, b, c):
    delta = math.pow(b,2) - 4 * a * c
    x1 = (-b + math.sqrt(delta)) / (2*a)
    x2 = (-b - math.sqrt(delta)) / (2*a)
    return x1,x2

x1,x2 = quadratic(1,-3,2)
print(x1,x2)

# 默认参数
def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L

print(add_end())
print(add_end())

# 可变参数
# 允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple
def calc(*number):
    sum = 0
    for x in number:
        sum += x * x
    return sum
print(calc())
print(calc(1,2))
L = [1,2,3]
print(calc(*L))

# 关键字参数
# 允许传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict
def person(name,age,**kw):
    print('name:',name,'age:',age,'other:',kw)

person('Caoqi',24,city = 'Chengdu')
extra = {'city':'Chengdu','job':'IT'}
person('Caoqi',24,**extra)

# 命名关键字参数
# 如果要限制关键字参数的名字，就可以使用命名关键字参数
# 采用*作为分隔符，*后面的参数被视为命名关键字参数
def person1(name,age,*,city,job):
    print(name,age,city,job)

person1('Caoqi',24,city = 'Chengdu',job = 'IT')

# practice
def hello(greeting,*args):
    if (len(args)==0):
        print('%s!'% greeting)
    else:
        print('%s,%s!' % (greeting,','.join(args)))

hello('Hi')
hello('Hi','Caoqi')
hello('Hi','Caoqi','Wcy')

def print_scores(**kw):
    print('      Name  Score')
    print('---------------------')
    for name,score in kw.items():
        print('%10s  %d' % (name,score))
    print()

print_scores(Caoqi = 1,Wcy = 2)

# 递归函数
def move(n,a,b,c):
    if (n==1):
        print(a,'-->',c)
    else:
        move(n-1,a,c,b)
        move(1,a,b,c)
        move(n-1,b,a,c)

move(3, 'A', 'B', 'C')
