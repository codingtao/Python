# 1 返回函数
# 闭包

# 2 匿名函数（我理解为python内部的lambda表达式）
# 关键字lambda表示匿名函数，lambda x: x * x实际上就是
# def f(x):
#   return x * x
# 匿名函数也是一个函数对象，也可以把匿名函数赋值给一个变量，再利用变量来调用该函数
f = lambda x: x * x
print(f(5))

# 3 装饰器
# 函数对象有一个__name__ 属性，可以拿到函数的名字
# 假设我们要增强函数的功能（比如在函数调用前后打印日志），但又不希望修改原函数的定义
# 这种在代码运行器件动态增加功能的方式，称之为“装饰器”（Decorator）
import functools

def log(func):
    @functools.wraps(func) # functools内建模块的wraps函数，可以将函数func的__name__属性恢复
    def wrapper(*args,**kw):
        print('call %s' % func.__name__)
        return func(*args,**kw)
    return wrapper

@log
def now():
    print('2017-7-19')

now()
print('now.name = '+ now.__name__)

# decorator需要传入参数的情况
def log1(text):
    def decorator(func):
        def wrapper(*args,**kw):
            print('%s %s()' % (text,func.__name__))
            func(*args,**kw)
        return wrapper
    return decorator

@log1('excute')
def now1():
    print('2017-7-19')
now1()
print('now1.name = '+ now1.__name__)
 
# 4 偏函数
# 作用：把一个函数的某些参数给固定住（也就是设置默认值），返回一个新的函数，调用这个新函数会更简单。
# 创建偏函数时，实际上可以接收函数对象、*args和**kw这3个参数
# functools.partial就是帮助我们创建一个偏函数的
import functools
int2 = functools.partial(int,base = 2)　#int 为函数，base int函数中固定的变量　
print(int2('101'))