# 1 枚举类
# 建议参考：http://www.cnblogs.com/ucos/p/5896861.html
# Enum可以把一组相关常量定义在一个class中，且class不可变，而且成员可以直接比较。
# 用于定义枚举的class和定义类的class是有区别

from enum import Enum, unique

@unique
class Weekday(Enum):
    Sun = 0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6

day1 = Weekday.Mon

print('day1 =', day1)
print('Weekday.Tue =', Weekday.Tue)
print('Weekday[\'Tue\'] =', Weekday['Tue'])
print('Weekday.Tue.value =', Weekday.Tue.value)
print('day1 == Weekday.Mon ?', day1 == Weekday.Mon)
print('day1 == Weekday.Tue ?', day1 == Weekday.Tue)
print('day1 == Weekday(1) ?', day1 == Weekday(1))

for name, member in Weekday.__members__.items():
    print(name, '=>', member)

Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)

# 2 使用元类
# 动态语言和静态语言最大的不同，就是函数和类的定义，不是编译时定义的，而是运行时动态创建的
# type():type()函数既可以返回一个对象的类型，又可以创建出新的类型
# 要创建一个class对象，type()函数依次传入3个参数：
# class的名称；
# 继承的父类集合，注意Python支持多重继承，如果只有一个父类，别忘了tuple的单元素写法；
# class的方法名称与函数绑定，这里我们把函数fn绑定到方法名hello上。
# 例：
def fn(self,name = 'world'):
    print('hello,%s' % name)

Hello = type('Hello',(object,),dict(hello=fn))
h = Hello()
h.hello()

# 元类：
# metaclass : 除了使用type()动态创建类以外，要控制类的创建行为，还可以使用metaclass;
# 当我们定义了类以后，就可以根据这个类创建出实例，所以：先定义类，然后创建实例
# 但是如果我们想创建出类呢？那就必须根据metaclass创建出类，所以：先定义metaclass，然后创建类
# 连接起来就是：先定义metaclass，就可以创建类，最后创建实例
# 所以，metaclass允许你创建类或者修改类。换句话说，你可以把类看成是metaclass创建出来的“实例”
# 有点难理解，先跳过（魔法函数啊!!）
