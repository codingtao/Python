# 3 多重继承
# MixIn

# 4 定制类
# __str__
# __repr__
# __iter__  :如果一个类想被用于for ... in循环，类似list或tuple那样，就必须实现一个__iter__()方法，该方法返回一个迭代对象
# __getitem__: 要表现得像list那样按照下标取出元素，需要实现__getitem__()方法：
# __setitem__():把对象视作list或dict来对集合赋值
# __delitem__():用于删除某个元素。
# __getattr__():动态返回一个属性,注意：只有在没有找到属性的情况下，才调用__getattr__，已有的属性，比如name，不会在__getattr__中查找。
# __call__():一个对象实例可以有自己的属性和方法，当我们调用实例方法时，我们用instance.method()来调用。类中定义__call__()直接在实例本身上调用

# 1
# class Student(object):
#     def __init__(self,name):
#         self._name = name
#     def __str__(self):
#         return 'Student object (name : %s)' % self._name
#     __repr__ = __str__
# print(Student('Tony'))

# 2 把一个类设计可以类似list一样调用
class Fib(object):
    def __init__(self):
        self._a , self._b = 0 , 1 # 初始化计数器_a _b
    
    def __iter__(self):
        return self # 实例本身就是迭代对象，故返回自己

    def __next__(self):
        self._a , self._b = self._b , self._a + self._b #计算下一个值
        if self._a > 100: # 退出循环的条件
            raise StopIteration()
        return self._a #返回下一个值

    def __getitem__(self,n):
        if(isinstance(n,int)): # n是索引
            _a,_b = 1,1
            for x in range(n):
                 _a,_b = _b,_a+_b
            return _a

        if(isinstance(n,slice)):# 你是切片
            print('start %d' % n.start)
            print('stop %d' % n.stop)   
                     
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            _a,_b = 1, 1
            L = []
            for x in range(stop):
                if x>=start:
                    L.append(_a)
                _a,_b = _b,_a+_b
            return L
            
for n in Fib():
    print(n)

print(Fib()[3])
print(Fib()[0:3])


# 3
print('*******3*******\n')
class Student(object):
    def __init__(self):
        self.name = 'Tony'
    def __getattr__(self,attr):
        if attr == 'score':
            return 99
        raise AttributeError('Student has no attribute %s' % attr)
     
s = Student()
print(s.name)
print(s.score)

# practice
class Chain(object):
    def __init__(self,path=''):
        self._path = path
    def __getattr__(self,path):
        return Chain('%s/%s' % (self._path,path))
    def __call__(self,name):
            return Chain('%s/%s' % (self._path,name))
    def __str__(self):
        return self._path

    __repr__ = __str__


print(Chain().status.user.timeline.list) # '/status/user/timeline/list'
print(Chain().users('michael').repos) #'/user/michael/repos'