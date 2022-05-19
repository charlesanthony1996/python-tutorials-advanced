#and or do not return bools in python

def do_something(arg=None):
    arg = arg or []


if __name__ == "__main__":
    print(0 or [] or {})
    print(1 or 1 or 2)
    
    print(1 and 2 and 3)
    print(1 and 0 and [])