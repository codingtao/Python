# 面向对象编程
# 类与实例 __init__方法（类似类的构造方法））  def __init__(self,name,score)
# 数据封装：类的方法 def fun(self): 必须有self 参数
# 访问限制：私有变量 __name
# 继承和多态：class B(A):  注意动态语言的鸭子类型：一个对象只要“看起来像鸭子，走起路来像鸭子”，那它就可以被看做是鸭子。
# 
# 获取对象信息：isinstance type dir  以及  getattr setattr hasattr
# 实例属性于类属性： 
# 给实例绑定属性的方法是通过实例变量，或者通过self变量：
# class Student(object):
#    def __init__(self, name):
#        self.name = name
# 
