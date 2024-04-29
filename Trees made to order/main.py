from binary_tree_printer import BinaryTreePrinter
from constants import NODE_NUM_MAX

def main():
    printer = BinaryTreePrinter(NODE_NUM_MAX)
    while True:
        order_num = int(input())
        if order_num == 0:
            break
        result = printer.print_tree(order_num)
        print(result)  

main()
