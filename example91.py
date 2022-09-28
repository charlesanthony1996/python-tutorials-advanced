import sys

def capacity(l: list):
    return (sys.getsizeof(l) - 56) // 8

def capacity_of_some_lists():
    x = []
    for i in range(100):
        x.append(i)
        print(f"{len(x)=}, {capacity(x)=}")


def compute_overallocation_ratios():
    x = [0]
    last_capacity = 1
    for _ in range(100000):
        x.append(0)
        new_capacity = capacity(x)
        if new_capacity != last_capacity:
            print(f"ratio={new_capacity / last_capacity:.3f}")
            last_capacity = new_capacity

    print(f"approaching {9/8=}")


def basic_compare_lists():
    x = [0, 0, 0]
    n = len(x)
    y = [0] * n
    z = [0 for _ in range(n)]

    x[:] = y[:] = z[:] = range(1000)
    x[:] = y[:] = z[:] = range(499)

    print(capacity(x))
    print(capacity(y))
    print(capacity(z))



def list_internal_structure():
    #garbage collection info (before object)
    _gc_next = ...
    _gc_prev = ...

    ob_recfnt = ...
    ob_type = ...

    ob_size = ...

    ob_item = ...
    allocated = ...


def getsizeof_list():
    n = 56
    n += 8 * allocated


def sizeof_some_lists():
    print(sys.getsizeof([]))

def main():
    basic_compare_lists()


if __name__ == "__main__":
    main()


