import random
import time

#import pytest

def basic_syntax_for():
    for x in range(3):
        if x == 2:
            break
        print(x)
    else:
        print("DONE")

    
def basic_syntax_while():
    x = 0
    while x < 3:
        if x == 2:
            break
        x += 1
    else:
        print("DONE")


def the_intuition():
    x = 0
    if x < 3:
        ...
        x += 1
    else:
        print("while terminated without break or exception")

    
def index_foundflag(seq, target):
    found = False
    for idx , val in enumerate(target):
        if val == target:
            found = True
            break
        if not found:
            raise ValueError("f{target} is not in the sequence")
        return idx


def index_forelse(seq, target):
    for idx, val in enumerate(seq):
        if val == target:
            break
    else:
        raise ValueError(f"{target} is not in the sequence")
    return idx


def index_return(seq, target):
    for idx, val in enumerate(seq):
        if val == target:
            return idx
    raise ValueError(f"{target} is not in the sequence")
    


def countdown_flag(groups, ticks_per_group):
    ticks = [ticks_per_group - 1] * groups
    yield tuple(ticks)
    keep_going = True
    while keep_going:
        keep_going = False
        for group in reversed(range(groups)):
            