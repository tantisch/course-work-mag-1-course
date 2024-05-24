from tree_printer import TreePrinter
from tree_converter import TreeConverter
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
        tree = TreeConverter.from_string(result, max_children)
        print(tree)
        tree.visualize_networkx()
        if max_children == 2:
            bst_tree = tree.to_bst()
            print("BST:", bst_tree)
            bst_tree.visualize_networkx()
            while True:
                value = int(input("Enter a value to search in BST (or enter 0 to stop): "))
                if value == 0:
                    break
                found = bst_tree.search(value)
                print(f"Value {'found' if found else 'not found'} in the BST.")
        elif max_children == 3:
            tst_tree = tree.to_tst()
            print("TST:", tst_tree)
            tst_tree.visualize_networkx()
            while True:
                value = int(input("Enter a value to search in TST (or enter 0 to stop): "))
                if value == 0:
                    break
                found = tst_tree.search(value)
                print(f"Value {'found' if found else 'not found'} in the TST.")
main()


main()
