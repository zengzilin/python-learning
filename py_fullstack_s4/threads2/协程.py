import time

#  可以实现并发


def consumer():

    r = ''
    while True:

        n = yield r
        if not n:
            return
        print('[CONSUMER] ←← Consuming %s...' % n)
        time.sleep(1)
        r = '200 OK'

def produce(c):

    next(c)
    n = 0
    while n < 5:
        n = n + 1
        print('[PRODUCER] →→ Producing %s...' % n)

        cr = c.send(n)

        print('[PRODUCER] Consumer return: %s' % cr)

    c.close()

if __name__=='__main__':

    c = consumer()
    produce(c)
