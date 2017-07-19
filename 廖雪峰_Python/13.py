# 面向对象的高级编程

# 1 __slots__
# 目的： 限制实例的属性
# class Student(object):
#    __slots__ = ('name', 'age') # 用tuple定义允许绑定的属性名称
# 注意：使用__slots__要注意，__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的：

class Student(object):
    __slots__ = ('name', 'age') # 用tuple定义允许绑定的属性名称

class GraduateStudent(Student):
    pass

s = Student() # 创建新的实例
s.name = 'Michael' # 绑定属性'name'
s.age = 25 # 绑定属性'age'
# ERROR: AttributeError: 'Student' object has no attribute 'score'
try:
    s.score = 99
except AttributeError as e:
    print('AttributeError:', e)

g = GraduateStudent()
g.score = 99
print('g.score =', g.score)


# 2 使用@property
# Python内置的@property装饰器就是负责把一个方法变成属性调用的：

# practice
class Screen(object):
    
    @property
    def width(self):
        return self._width

    @width.setter
    def width(self,value):
        self._width = value
    
    @property
    def height(self):
        self._height

    @height.setter
    def height(self,value):
        if not isinstance(value,int):
            raise ValueError('width must be an integer!')
        self._height = value
    
    @property
    def resolution(self):
        return self._width * self._height


s = Screen()
s.width = 1024
s.height = 768
print(s.resolution)
assert s.resolution == 786432, '1024 * 768 = %d ?' % s.resolution

# 3 多重继承
# MixIn

# 4 定制类
# __str__
# __repr__
# __iter__  :如果一个类想被用于for ... in循环，类似list或tuple那样，就必须实现一个__iter__()方法，该方法返回一个迭代对象
# __getitem__: 要表现得像list那样按照下标取出元素，需要实现__getitem__()方法：
# __setitem__():把对象视作list或dict来对集合赋值
# __delitem__():用于删除某个元素。

# 例子 REST API 常用
class Chain(object):
    
    def __init__(self,path=''):
        self._path = path
    
    def __getattr__(self,path):
        return Chain('%s/%s' % (self._path,path))

    def __str__(self):
        return self._path

    __repr__ =__str__

print(Chain().status.user.timeline.list)