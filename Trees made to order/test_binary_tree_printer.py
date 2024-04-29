from binary_tree_printer import BinaryTreePrinter
from constants import NODE_NUM_MAX


def test_binary_tree_printer():
    printer = BinaryTreePrinter(NODE_NUM_MAX)

    assert printer.print_tree(1) == "X"
    assert printer.print_tree(2) == "X(X)"
    assert printer.print_tree(3) == "(X)X"

    assert printer.print_tree(4) == "X(X(X))"
    assert printer.print_tree(5) == "X((X)X)"
    assert printer.print_tree(6) == "(X)X(X)"
    assert printer.print_tree(7) == "(X(X))X"
    assert printer.print_tree(8) == "((X)X)X"
    assert printer.print_tree(9) == "X(X(X(X)))"

    assert printer.print_tree(20) == "((X)X(X))X"

test_binary_tree_printer()
print("All tests passed!")
    