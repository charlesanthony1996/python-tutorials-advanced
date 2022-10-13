from __future__ import annotations

import typing

class Node:
    data:int
    next: Node | None


print(Node.__annotations__)
print(typing.get_type_hints(Node))
print("Hello, World!")

def sub():
    yield 2
    return
    yield 3


def main():
    yield 1
    subgen = sub()
    yield next(subgen)
    yield next(subgen) #raises stopIteration
    yield 4

# for x in gen():
#     print(x)

