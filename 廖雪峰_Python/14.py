# 2 使用@property
# Python内置的@property装饰器就是负责把一个方法变成属性调用的：

# class Student(object):
#     def get_score(self):
#         return self._score

#     def set_score(self,value):
#         if not isinstance(value,int):
#             raise ValueError('score must be integer')
#         if value <0 or value>100:
#             raise ValueError('score must between 0~100')
#         self._score = value

# s = Student()
# s.set_score(60)
# print('%d' % s.get_score())

# 为了既能检查参数 又能像直接调用属性一样使用  引入装饰器 property
# property 负责把一个方法变成属性调用
# 把一个getter方法变成属性，只需要加上@property就可以了
# 此时，@property本身又创建了另一个装饰器@score.setter,负责把一个setter方法变成属性赋值

class Student(object):
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self,value):
        if not isinstance(value,int):
            raise ValueError('score must be integer')
        if value < 0 or value > 100:
            raise ValueError("score must between 0 ~ 100")     
        self._score = value

s = Student()
s.score = 60
print('%d' % s.score)

# practice
class Screen(object):
    
    @property
    def width(self):
        # 可以添加参数检查
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