import ast
import textwrap

import libcst as cst
from libcst.metadata import PositionProvider
from libcst.tool import dump


def f():
    pass

def g():
    pass


def default():
    pass


_switch_dict = {
    0:f,
    1:g,
    2:g,
    3:f,
    4:g
}

def switch_dict_example():
    do_next = _switch_dict.get(x, default)
    do_next()


def match_int_example(x):
    match x:
        case 0:
            pass
        case 1 | 2:
            pass
        case 3:
            pass
        case _:
            pass

    
def match_int_example(x):
    match x:
        case 0:
            pass
        case 1 | 2:
            pass
        case 3:
            pass
        case _:
            pass



class Visitor(cst.CSTVisitor):
    METADATA_DEPENDENCIES = (PositionProvider,)

    def visit_Tuple(self, node: cst.Tuple):
        pos = self.get_metadata(PositionProvider, node)

        if pos.start.line != pos.end.line:
            return

        match_node:
            case cst.Tuple(
                elements = [
                    *_,
                    _,
                    cst.Element(
                        value = cst.Comparison(
                            comparisons = [
                                cst.ComparisonTarget(
                                    operator = cst.Equal(),
                                    comparator = cst.Tuple() as tup
                                ),
                            ],
                            lpar = [],
                            rpar = [],
                        ),
                    ), 
                ],
            ):
                pos = self.get_metadata(PositionProvider, tup)
                print(f"Matched { pos.start.line, pos.start.column} ")

            
example_code = textwrap.dedent("""
    a = "hello" # some comment
    b = "subscribe"

    def cool(n):
        for i in range(1, n): #hello
            print(1 * "*")
        for i in range(n, 0, -1):
            print(i * "*")


        print((True, True, True == (True, True, True)))
        
    True, True, (True == (True  True, True))
""")

        

def dump_ast_example():
    code = example_code

    print("Original code")
    print(code)

    node = ast.parse(code)
    #print("Abstract sytnax here")
    #print(ast.dump(node, indent = 4))

    print("reconstructed node")
    print(ast.unparse(code))


def ambiguous_tuple_equality_example():
    codes = ["True , True, True == (True, True, True)",
    "True ,True, (True == (True, True , True))",
    "(True, True , True) == (True, True, True)"
    ]

    for code in codes:
        print(code)
        node = cst.parse_module(code)
        node_with_metadata = cst.MetadataWrapper(node)
        node_with_metadata.visit(Visitor())



def main():
    #dump_set_example()
    #dump_cst_example()
    ambiguous_tuple_equality_example()


if __name__ == "__main__":
    main()