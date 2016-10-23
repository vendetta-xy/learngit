#！/usr/bin/env python3
#-*-coding:utf-8 -*-

def consumer():
    r=''
    while True:
        n=yield r
        if not n:
            return
        print('[CONSUMER]Consuming %s...'% n)
        r='200 OK'

def produce(c):
    c.send(None)
    n=0
    while n<5:
        n=n+1
        print('[PRODUCER] Produciing %s...' %n)
        r=c.send(n)
        print('[PRODUCER] Consumer return: %s'% r)
    c.close()

c=consumer()
produce(c)


'''def countdown(n):
    print('Counting down from',n)
    while n>=0:
        newvalue =(yield n)
        if newvalue is not None:
            n=newvalue
        else:
            n-=1
c=countdown(5)
for x in c:
    print (x)
    if x==5:
        c.send(3)
        
'''
