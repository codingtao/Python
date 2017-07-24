# 序列化
# 我们把变量从内存中变成可存储或传输的过程称之为序列化，在Python中叫pickling
# 序列化之后，就可以把序列化后的内容写入磁盘，或者通过网络传输到别的机器上
# 反过来，把变量内容从序列化的对象重新读到内存里称之为反序列化，即unpickling

# pickle.dumps():把任意对象序列化成一个bytes，然后，就可以把这个bytes写入文件
# pickle.loads()
# pickle.dump():直接把对象序列化后写入一个file-like Object
# pickle.load()


# 例子
import pickle
# d =  dict(name = 'Tony',age = 25,score = 100)
# with open('./test.txt','wb') as f:
#     pickle.dump(d,f)

# with open('./test.txt','rb') as f:
#     d = pickle.load(f)
# print(d)

import json
# d =  dict(name = 'Tony',age = 25,score = 100)
# print(json.dumps(d))
# json_str = '{"score": 100, "age": 25, "name": "Tony"}'
# print(json.loads(json_str))
class Student(object):
    def __init__(self,name,age,score):
        self._name = name
        self._age = age
        self._score = score

s = Student('Tony',25,100)
print(json.dumps(s,default = lambda obj:obj.__dict__))
json_str = '{"age": 20, "score": 88, "name": "Bob"}'

def dict2student(d):
    return Student(d['name'],d['age'],d['score'])

print(json.loads(json_str,object_hook=dict2student))