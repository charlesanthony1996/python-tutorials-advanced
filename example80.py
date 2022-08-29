import sys
from collections import deque
from collections.abc import Set, Mapping
from numbers import Number
from timeit import timeit
#from pympler.asizeof import asizeof as getsize

#import pytest

def normal_class_example():
    print("Normal class example")

    class A:
        v = 42

        def __init__(self):
            self.x = "hello"

    a = A()
    print("a dict: ", a.__dict__)


    print("a.x (looked up in a dict):", a.x)
    a.x = "world"
    print("a.x (looked up in a dict):", a.x)

    print("a.v (not found in a, looked up in A", a.v)

    with pytest.raises(AttributeError):
        a.y

    a.y = ":)"
    print("a.y", a.y)

    with pytest.raises(AttributeError):
        a.w

    A.w = "class variable"
    print("a.w (not found in a, looked up in A", a.w)


def slots_class_example():
    print("slots class example")

    class A:
        __slots__= ("x",)

        def __init__(self):
            self.x = 42

    print("size of A instance", sys.getsizeof(A))
    print("size of B instance", sys.getsizeof(B))
    print()

    print("recursive size of A instance:", getsize(A()))
    print("recursive size of B instance:", getsize(B()))
    print("size A /size B", getsize(A()) / getsize(B()))


def why_really_use_slots_example():
    print("Why really use slots example")

    class A:
        def __init__(self):
            self.x = 42
            self.y = 42
            self.z = 42
            self.t = 42
            self.u = 42
            self.v = 42
            self.w = 42

    class B:

        __slots__ = "x", "y", "z", "t", "u", "v", "w"

        def __init__(self):
            self.x = 42
            self.y = 42
            self.z = 42
            self.t = 42
            self.u = 42
            self.v = 42
            self.w = 42

        
    print("size of a instance: ", sys.getsizeof(A()))
    print("size of b instance: ", sys.getsizeof(B()))

    print()
    print("recursive of size of A instance: ", getsize(A()))
    print("recursive of size of B instance: ", getsize(B()))
    print("size A / size B", getsize(A() /getsize(B())))
    print()



def slots_speed_considerations():
    print("slots speed considerations")


    class A:
        def __init__(self):
            self.x = 42

    class B:
        __slots__ = ("x",)

        def __init__(self):
            self.x = 42


    number = 10_000_000
    create_time = timeit(stmt="a=A()", globals =locals(), number = number)
    slotted_create_time = timeit(stmt= "bB()", globals=locals() , number = number)

    get_time = timeit(setup="a=A()", stmt = "a.x" , globals =locals(), number = number)
    slotted_get_time = timeit(setup="b=B()", stmt = "b.x", globals=locals(), number = number)

    set_time = timeit(setup="a=A()", stmt = "a.x = 0", globals=locals(), number = number)
    slotted_set_time = timeit(setup="b=B()", stmt="b.x", globals=locals(), number = number)

    #all close , not a reason to choose slots

    print(f"{create_time=}")
    print(f"{slotted_create_time=}")
    print(f"{get_time=}")
    print(f"{slotted_get_time=}")
    print(f"{set_time=}")
    print(f"{slotted_set_time=}")


def how_slots_work_example():
    print("how slots work example")
    
    class A:
        pass

    class B:
        __slots__ = "x", "y", "z"


    print("A dict: ", A.__dict__)
    print("B dict: ", B.__dict__)
    print("B.x:", B.x)

    b = B()
    b.x = "subscribe"
    print(b.x)


class Member:
    def __get__(self, instance, owner):
        if owner is None:
            return self

        val = ...
        return val

    def __set__(self, instance, value):
        pass


def what_is_a_slot_example():
    pass






