from run_mp import run_mp

def useful_func(x):
    return x * x


print("main func", __name__)

run_mp(useful_func, [1, 2, 3, 4])
