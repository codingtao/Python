# 1 IO
# Python引入了with语句来自动帮我们调用close()方法,从而不必调用f.close()方法    
# with open('/path/to/file', 'r') as f:
#     print(f.read())

with open('./test.txt','w') as f:
    f.write('傻逼cq')

# 2 StringIO
# StringIO顾名思义就是在内存中读写str
from io import StringIO
f = StringIO()
print(f.write('hello'))
print(f.getvalue())

f = StringIO('hello\nhi\ngoodbye')
print(f.tell())
while True:
    s = f.readline()
    if s == '':
        break
    print(s.strip())

# 3 ByteIO  
# StringIO操作的只能是str，如果要操作二进制数据，就需要使用BytesIO

# 4 操作文件和目录
# 操作文件和目录的函数一部分放在os模块中，一部分放在os.path模块中，这一点要注意一下。查看、创建和删除目录可以这么调用：
# import os,sys
# print(os.path.abspath(sys.argv[0]))

# os.path.join
# os.path.split
# os.path.splitext
# os.mkdir
# os.rmdir



import os
abspath = os.path.abspath('.')
print(abspath) #查看当前目录的绝对路径
# 在某个目录下创建一个新目录，首先把新目录的完整路径表示出来：
newdirpath =  os.path.join(abspath,'testdir') #注意：把两个路径合成一个时，不要直接拼字符串，而要通过os.path.join()函数，这样可以正确处理不同操作系统的路径分隔符
# 然后创建一个新目录
# os.mkdir(newdirpath)
# 删除一个目录
# os.rmdir(newdirpath)

newdir = os.path.split(newdirpath) #注意：要拆分路径时，也不要直接去拆字符串，而要通过os.path.split()函数，这样可以把一个路径拆分为两部分，后一部分总是最后级别的目录或文件名
print(newdir[1])

# 列出当前目录下的所有目录
L = [x for x in os.listdir('.') if os.path.isdir(x)]
print(L)
# 列出所有的.txt文件
L = [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.txt']
print(L)