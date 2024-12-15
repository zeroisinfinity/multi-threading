from threading import Thread
import cProfile
import time
def func():
    for i in range(0,-999999,-1):
        print(i)
t1 = Thread(target=func)

class Test:
    def m1(self):
        for i in range(999999):
            print(i)

t2 = Thread(target=Test().m1)
'''s = time.time()
func()
Test().m1()
e = time.time()
print(e-s)'''
def w():
    t1.start()
    t2.start()
    t1.join()
    t2.join()
cProfile.run('w()')
#cProfile.run('t1.start()')
#cProfile.run('t2.start()')
