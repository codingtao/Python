# 用协程处理生产者－消费者模型

def consumer():
    r = ''
    while True:
        n = yield r
        if not n:
            return
        print('[CONSUMER] Consuming %s' % n)
        r = '200 OK'

def produce(c):
    c.send(None) # 等价于c.next(),用于启动生成器
    n = 0
    while n < 5:
        n = n + 1
        print('[PRODUCE] Producing %s' % n)
        r = c.send(n) # 把n传给consumer,从第６行开始，但是只赋值，不执行，从第７行开始执行，直到yield，返回ｒ
        print('[PRODUCE] Producing return %s' % r)
    c.close()

c = consumer()
produce(c)
