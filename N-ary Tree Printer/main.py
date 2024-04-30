from tree_printer import TreePrinter
from constants import NODE_NUM_MAX

def main():
    max_children = int(input('Please specify maximum number of children for each node: '))
    printer = TreePrinter(max_children=max_children, max_nodes=NODE_NUM_MAX)
    while True:
        order_num = int(input())
        if order_num == 0:
            break
        result = printer.print_tree(order_num)
        print(result)  


main()
