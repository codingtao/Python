# 模块

# Python中一个.py文件就是一个模块
# Python 中有内置模块 和 第三方模块

# Python 内置函数集合： 
# abs() 
# all(iterable) : 特别注意：空列表、空元祖返回True；非空列表或元祖，只要有None、''或0返回false(即 "全‘真’为True，有‘假’为False")
# any(iterable):特别注意：当iterable为空的时候，函数返回值为False   "全‘假’为False，有‘真’为True"
# ascii(object)
# bin(x) :Convert an integer number to a binary string
# bool([x]):bool(1)
# bytearray() bytes()
# chr(i)  i>=0 && i<=255 返回0-255内的字符
# classmethod() : classmethod 修饰符对应的函数不需要实例化，不需要 self 参数，但第一个参数需要是表示自身类的 cls 参数，可以来调用类的属性，类的方法，实例化对象等。
# complex(1,2): 1+2j  complex("1+2j")
# delattr() setattr()
# dict()  
# dir() 返回模块的属性列表
# divmod(a,b) 返回(a/b,a%b)
# enumerate()
# format: 新增了一种格式化字符串的函数 str.format()，它增强了字符串格式化的功能 基本语法是通过 {} 和 : 来代替以前的 % 
# id():函数用于获取对象的内存地址
# ord():返回字符的ascii码
# round():round() 方法返回浮点数x的四舍五入值
# type() : 获取对象的类型 type(abs)
# zip() 将可迭代对象组装成元祖
#

print(bin(5))
print(complex('1+2j'))
print(dir())
print("网站名：{name}, 地址 {url}".format(name="廖雪峰_Python", url="www.runoob.com"))
print(round(1.23344,2))

import sys
print(sys.path)