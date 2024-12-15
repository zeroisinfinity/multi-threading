import time
import threading
import cProfile
def test_multithreading():
    for i in range(999999):
        print(i)

def test_2():
    for i in range(999999):
        print(i)

def test_3():
    for i in range(999999):
        print(i)


"""
start_time = time.time()
test_multithreading()
test_3()
test_2()
end_time = time.time()"""

#print(end_time - start_time)

t1 = threading.Thread(target=test_multithreading)
t2 = threading.Thread(target=test_2)
t3 = threading.Thread(target=test_3)
start_time = time.time()

def test_th():
    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()
cProfile.run('test_th()')
'''test_multithreading()
test_2()
test_3()'''
end_time = time.time()

print('Done {}'.format(end_time - start_time))



