import time
import multiprocessing
import cProfile


# Replace print statements with computations or simulated work
def test_multiprocessing():
    for i in range(9999999):
        print(i)  # Simulate work


def test_2():
    for i in range(9999999):
        print(i)  # Simulate work


def test_3():
    for i in range(9999999):
        print(i)  # Simulate work


def test_mp():
    # Create processes
    p1 = multiprocessing.Process(target=test_multiprocessing)
    p2 = multiprocessing.Process(target=test_2)
    p3 = multiprocessing.Process(target=test_3)

    # Start processes
    p1.start()
    p2.start()
    p3.start()

    # Wait for processes to complete
    p1.join()
    p2.join()
    p3.join()


# Measure performance
if __name__ == '__main__':
    start_time = time.time()
    test_multiprocessing()
    test_2()
    test_3()
    end_time = time.time()

    # Profile the multiprocessing function
    s = time.time()
    test_mp()
    e = time.time()
    print('Execution Time without multithreading: {:.2f} seconds'.format(end_time - start_time))
    print('Execution Time with multithreading: {:.2f} seconds'.format(e - s))


