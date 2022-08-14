class BadList(list):

    def __add__(self, other):
        print("Running custom add")
        return BadList(super(BadList, self).__add__(other))
    
    def __iadd__(self, other):
        print("Running custom iadd")
        return self + other

    
def plusequals_may_change_pointers():
    x = 1
    print(id(x))
    print()
    x += 1
    print(id(x), "Changed")
    print()

    x = []
    print(id(x))
    x += [1]
    print(id(x), "Not Changed")

    bad = BadList()
    print(bad, "Before append")
    bad += [1, 2, 3]
    append_some_to_list(bad)
    print(bad, "after append")


def append_some_to_list(l):
    l += [4, 5, 6]


def plusequals_meaning(x, y):
    result = x.__iadd__(y)
    x = result

    result = x[0].__iadd__(y)
    x[0] = result.__iadd__(y)

    result = x.val.__iadd__(y)
    x.val = result


def tuple_what():
    pros_and_cons = (["subscribing helps james", "subscribing feels good"], ["i have to click"])

    pros = pros_and_cons[0]

    pros += ["big numbers are cool"]

    try:
        pros_and_cons[0] += ["james is cool"]
    
    except TypeError:
        print(pros_and_cons)


def main():
    plusequals_may_change_pointers()


if __name__ == "__main__":
    main()



