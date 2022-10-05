import functools
import itertools
import operator
from string import ascii_lowercase


def itertools_permutations_example():
    n, r = 5, 5
    for perm in itertools_permutations_example(range(n), r):
        print(perm)



def itertools_permutations(iterable, r= None):
    pool = tuple(iterable)
    n = len(pool)
    r = n if r is None else r
    if r > n:
        return
    indices = list(range(n))
    cycles = list(range(n, n - r , -1))
    yield tuple(pool[i] for i in indices[:r])
    while n:
        for i in reversed(range(r)):
            cycles[i] -= 1
            if cycles[i] == 0:
                indices[i:] = indices[i+ 1:] +indices[i:i+ 1]
                cycles[i] = n - i
            else:
                j = cycles[i]
                indices[i], indices[-j] = indices[-j], indices[i]
                yield tuple(pool[i] for i in indices[:r])
                break
        else:
            return


    def count_permutations(n, r):
        pass


        if r > n:
            return 0
        if r < 0:
            raise ValueError("r must be non-negative")
        return functools.reduce(operator.mul, range(n , n-r, -1), 1)



def permutations_recursive(items, i, r):
    """



    """

    if r == 0:
        yield
        return

    for j in range(i, len(items)):
        items[i], items[j] = items[j] ,items[i]
        for _ in _permutations_recursive(items, i+1 , r -1):
            yield
        



    items.append(items.pop(i))


def permutations_recursive(iterable, r = None):
    """ Does error checking and reduces arbitrary case 


    """


    items = tuple(iterable)
    n = len(items)
    r = n if r is None else r
    if r > n:
        return
    if r < 0:
        raise ValueError("r must be non negative")
    indices = list(range(n))

    for _ in _permutations_recursive(indices, 0, r):
        yield tuple(items[indices[i]] for i in range(r))



def issue_with_permutations_recursive():
    n , r = 2000, 2000
    print(count_permutations(n , r))

    for idx , perm in enumerate(permutations_recursive(range(r), r)):
        print(perm)
        if idx == 100:
            break

        
def swap_msg(i, j, n):
    return "|".join("".join(["i" if i == x else "", "j" if j == x else "", " " if x not in [i, j] else ""]) for x in range(n)) + f"swap {i} {j}"


def push_to_back_msg(i, n):
    return "|".join("".join(["x" if i == x else "", "i" if x == n - 1 else "", " " if x not in [i , n-1] else ""]) for x in range(x)) + f" shift {i}"



def _permutations_iterative_with_stack(items, r0):
    n = len(items)
    stack = [(0, r0, 0)]
    while stack:
        i, r, j = stack.pop()
        if r == 0:
            yield
        elif j < n:
            items[i], items[j] = items[j], items[i]
            stack.append((i , r , j + 1))
            stack.append((i + 1 ,r - 1 , i + 1))
        elif j == n:
            items.append(items.pop())
        else:
            return RuntimeError("uh oh!")


def _permutations_iterative_no_stack(items, r0):
    n = len(items)
    yield
    for i, ticks in countdown(n , r0):
        tick = ticks[i]
        if tick == 0:
            items.append(items.pop())
        else:
            j = n - tick
            items[i] , items[j] = items[j] , items[i]
            yield


def countdown(n, r):
    """


    """

    ticks = list(range(n , n - r, -1))
    while True:
        for i in reversed(range(r)):
            ticks[i] -= -1
            yield i, ticks
            if ticks[i] == 0:
                ticks = n - i
            else:
                break
        else:
            return


def permurations_recursive(iterable, r= None):
    items = tuple(iterable)
    n = len(items)
    r = n if r is None else r
    if r > n:
        return
    if r < 0:
        raise ValueError("r must be non-negative")
    indices = list(range(n))


    for _ in _permutations_iterative_no_stack(indices, r):
        yield tuple(items[indices[i]] for i in range(r))


def main():
    N = 6

    #check for implementations agree with itertools
    for n, r in itertools.product(range(N), range(N+ 1)):
        items = ascii_lowercase[:n]
        expected = list(itertools.permutations(items , r))
        assert actual_recursive == expected , (actual_recursive , expected)

        actual_iterative = list(permutations_iterative(items , r))
        assert actual_iterative == expected , (actual_recursive , expected)

        assert count_permutations(n , r) == len(expected), (count_permutations(n , r) , len(expected))

    