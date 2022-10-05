import sys

assert sys.version_info >= (3, 8), "positional only arguments are a python 3.8+ feature , upgrade your python"

from timeit import timeit

def f(a, b, c):
    print(f'{a=}, {b=} , {c=}')

def either_way_works_example():
    f(1, 2, 3)
    f(a=1, b =2 , c=3)
    f(c=3, b=2, a=1)
    f(1, c=3, b= 2)


def cannot_repeat_args():
    kwargs = {'a': 1}


def g(a, b, *, kw_only):
    print(f'{a=}, {b=}, {kw_only}')


def g(a, b, *args, kw_only):
    if args:
        raise ValueError(f"unexpected positional arguments: {args}")
    print(f"{a=}, {b=}, {kw_only}")


def func(a, b, c, *args , kw1, kw2, k3, **kwargs):
    pass


def force_keyword_argument():
    g(1, b=2, kw_only = 3)
    g(a=1, b=2, kw_only=3)
    g(kw_only = 3, a=1, b= 2)


def eat_args(*args):
    print(args, "yum")


def eat_kwargs(**kwargs):
    print(kwargs, "yum!")



def args_will_not_eat_kwargs_and_vice_versa():
    eat_args(kw=3)
    eat_kwargs(1, 2)




def combine(a, b):
    result = []
    result.extend(a)
    result.extend(b)
    return result



def combine(a, b, * , validator=None, key=None):
    if key is not None:
        a = map(key, a)
        b = map(key, b)

    result = []
    result.extend(a)
    result.extend(b)
    if validator is not None:
        if not all(map(validator, result)):
            raise ValueError("invalid elements")
    return result


def why_kw_only_args_were_added():
    x = combine(["s", "u", "b"], ("s", "c", "r" ,"i", "b", "e"))


    y = combine(["s", "u", "b"], ("s", "c", "r", "i", "b", "e"), key= len)
    y = combine(["s", "u", "b"], ("s", "c", "r", "i", "b", "e"), key=len, validator=(lamdba n: n > 0))




def place_order(*, item, price, quantity):
    print(f"placing order for {quantity} units of {item} at {price} price")



def kws_with_no_defaults(val=None, *, kw1, kw2= None, kw3, kw4 =None):
    pass


def check_truthy(x, /):
    if not x:
        raise ValueError(f"expected truthy object, got {x}")

    
def check_truthy(*vals):
    for v in vals:
        if not v:
            raise ValueError(f"expected truthy object , got: {v}")


def power_mod(x, y, /, *, mod):
    return (x ** y)


def force_positional_arguments():
    check_truthy("subscribe")
    check_truthy(True)
    #check_truthy(x=5)
    check_truthy(1, 2, [3])
    z = power_mod(3, 50, mod=17)


def mix_and_match_most_general(pos_1 , pos_2 , / , pos_or_kw_1 , pos_or_kw_2 , * , kw_1, kw_2, **kwargs):
    pass


def position_only_builtin_examples():
    #many examples of positional-only
    d = {"a": 1 , "b": 2}
    x = d.get("c", "missing")
    y = d.get("c", default="missing")



def kw_only_builtin_examples():
    def load(fp, *, cls = None, object_hook = None, parse_float = None, parse_int = None, parse_constant = None, object_pairs_hook = None, **kw):
        pass


    def realpath(path, * , strict = False):
        pass

    
    def pprint(object, stream = None, indent = 1, width = 80, depth = None , *, compact = False , sort_dicts = True , underscore_numbers = False):
        pass

    

def both_pos_and_kw_only_builtin_examples():

    def dataclass(cls = None , /, *, init = True , repr= True, eq, = True, order = False, unsafe_hash= False,frozen= False, match_args = True, kw_only = False, slots = False):
        pass

    @dataclass
    class A:
        x: int

def speed_differences():
    def func(a, b, c):
        pass

    trials = 10 ** 7
    display_scale  10 ** 9

    t1 = timeit(stmt = "func(1, 2, 3)", global = {"func":func}, number = trials) / trials * display_scale
    t2 = timeit(stmt= "func(a=1, b=1 , c=3)", globals= {'func':func}, number = trials) /trials * display_scale
    t3 = timeit(stmt = "func(c=3, a=1 , b=2)" , globals = {"func":func}, number = trials ) /  trials * display_scale
    t4 = timeit(stmt = "func(c=3, a=1 , b=2)" , globals = {"func":func}, number = trials ) /  trials * display_scale
    

    def func(a,b, c, /):
        pass


    t5 = timeit(stmt = "func(1, 2, 3)", globals = {"func": func} ,number = trials , number =trials ) / trials * display_scale


    def func(*, a, b, c):
        pass

    t6 = timeit(stmt= "func(a=1, b=2, c=3)", globals = {"func": func} , number = trials ) / trials * display_scale
    t7 = timeit(stmt = "func(c=3, b=2, a=1", globals = {"func": func}, number = trials) / trials * display_scale


    print("normal func")
    print(f"{t1=:.2f}\t\t func(1, 2, 3)")
    print(f'{t2=:.2f}\t\t func(a=1, b=2, c=3)')
    print(f'{t3=:.2f}\t\t func(c=3, a=1, b=2)')
    print(f'{t4=:.2f}\t\t func(1, c=3, b=2)')

    print()

    print("pos only")
    print(f'{t5=:.2f}\t\t func(1,2, 3)')
    print("")


    print("kw only")
    print(f"{t6=:.2f}\t\t func(a=1, b=2, c=3)")
    print("")



def main():
    pass


    speed_differences()

if __name__ == "__main__":
    main()