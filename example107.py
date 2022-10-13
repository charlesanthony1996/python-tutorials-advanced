import dataclasses
import functools

# import sqlalchemy.orm
# from pydantic import BaseModel

DESCRIPTOR_KEYS = {"__get__", "__set__", "__delete__"}


def descriptor_keys(obj):
    return DESCRIPTOR_KEYS & set(dir(obj))

def print_obj_and_descriptor_keys(obj):
    print(obj)
    keys = descriptor_keys(obj)
    if keys:
        print(f"is a descriptor: {keys}")
    else:
        print(f"Is not a descriptor, found: {keys}")


class Descriptor:
    def __get__(self, obj, objtype=None):
        ...
    def __set__(self, obj, value):
        ...
    def __delete__(self, obj):
        ...



class SomeClass:
    x = Descriptor()



def what_are_descriptors():
    obj = SomeClass()

    print(obj.x)
    print(SomeClass.x)

    obj.x = 42
    del obj.x


# functions

class A:
    def f(self):
        pass

    
def functions():
    print_obj_and_descriptor_keys(A.__dict__["f"])
    a = A()
    print(a.f)
    print(A.f)


#2 properties

class Rect:
    def __init__(self, w , h):
        self.width = w
        self.height = h

    @property
    def area(self):
        return self.width * self.height

    @functools.cached_property
    def expensive_val(self):
        return ...


class Student:
    def __init__(self, name):
        self.name = name
    
    @property
    def name(self):
        return self._name



def properties():
    print_obj_and_descriptor_keys(Rect.__dict__["area"])
    rect = Rect(2, 4)
    print(rect.area)

    student = Student("James")
    print(student.name)


class Property:
    def __init__(self, fget):
        self.fget = fget

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        return self.fget(obj)


#3 class methods and static methods

class Animal:
    @classmethod
    def create(cls):
        return cls()

    @staticmethod
    def something_static():
        ...

    
def static_and_class_methods():
    print_obj_and_descriptor_keys(Animal.__dict__["create"])
    animal = Animal.create()
    other = animal.create() #weird but okay


class ClassMethod:
    def __init__(self, f):
        self.f = f


    def __get__(self, obj, objtype=None):
        if objtype is None:
            objtype = type(obj)
        return self.f.__get__(objtype, objtype)


class StaticMethod:
    def __init__(self, f):
        self.f = f

    def __get__(self, obj , objtype = None):
        return self.f



class Vec3:
    __slots__ = ("x", "y", "z")


    def __init__(self, x, z):
        self.x = x
        self.y = y
        self.z = z


def slotted_variables():
    print_obj_and_descriptor_keys(Vec3.__dict__["x"])
    v = Vec3(0.0, 0.0, 0.0)
    v.x = 1.0



# 5. __dict__

class E:
    pass


def dunder_dict():

