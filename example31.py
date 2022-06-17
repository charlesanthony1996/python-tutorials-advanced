import timeit
import numpy as np

def while_loop(n= 100_000_000):
    i = 0
    s= 0
    while i < n:
        s += i
        i += 1
    return s

def for_loop(n = 100_000_000):
    s = 0
    for i in range(n):
        s += i
        i += 1
    return s


def for_loop_with_increment(n= 100_000_000):
    s = 0
    for i in range(n):
        s += i
        i += 1
    return s



def for_loop_with_test(n = 100_000_000):
    s = 0
    for i in range(n):
        if i < n:
            pass
        i += 1
        s += 1
    return s


def sum_range(n=100_000_000):
    return sum(range(n))


def sum_generator(n=100_000_000):
    return sum(i for i in range(n))

def sum_list_comp(n=100_000_000):
    return sum([i for i in range(n)])


def sum_numpy(n=100_000_000):
    return np.sum(np.arange(n, dtype=np.int64))


def sum_numpy_python_range(n=100_000_000):
    return np.sum(range(n))


def sum_math(n=100_000_000):
    return (n * (n-1))//2


def main():
    print(timeit.timeit(while_loop, number =1))
    print(timeit.timeit(for_loop, number =1))
    print(timeit.timeit(sum_range, number = 1))
    print(timeit.timeit(sum_generator, number =1))
    print(timeit.timeit(sum_list_comp,number =1))
    print(timeit.timeit(sum_numpy, number= 1))
    print(timeit.timeit(sum_numpy_python_range, number =1))
    print(timeit.timeit(sum_math,number =1))
    

    



if __name__ == "__main__":
    main()