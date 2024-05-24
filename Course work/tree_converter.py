from itertools import product
import networkx as nx
import matplotlib.pyplot as plt

class TreeConverter:
    def __init__(self, value, max_children=2):
        self.value = value
        self.children = [None] * max_children

    def __repr__(self):
        # children_repr = ", ".join(str(child) if child is not None else "None" for child in self.children)
        # return f"Tree({self.value}, [{children_repr}])"\
        return f"Tree({self.value}, {self.children})"

    @staticmethod
    def from_string(tree_str, max_children=2):
        if tree_str.isdigit():
            return int(tree_str)
        
        def parse_node(subtree_str):
            if subtree_str.isdigit():
                return int(subtree_str)
            value, children_str = subtree_str.split('(', 1)
            value = int(value)
            children_str = children_str[:-1]  # Remove trailing ')'
            children = []
            depth = 0
            child_str = ""
            for char in children_str:
                if char == ',' and depth == 0:
                    children.append(child_str)
                    child_str = ""
                else:
                    if char == '(':
                        depth += 1
                    elif char == ')':
                        depth -= 1
                    child_str += char
            children.append(child_str)  # Last child
            tree = TreeConverter(value, max_children)
            for i, child in enumerate(children):
                if child:
                    parsed_child = parse_node(child)
                    tree.children[i] = parsed_child
            return tree

        return parse_node(tree_str)

    def to_string(self):
        if all(child is None for child in self.children):
            return str(self.value)
        children_str = ",".join(child.to_string() if isinstance(child, TreeConverter) else str(child) for child in self.children)
        return f"{self.value}({children_str})"
    
    def to_bst(self):
        values = self._extract_values()
        values = sorted(set(values) - {0})  # Remove duplicates and 0, then sort
        self._build_bst(values)
        return self
    
    def _build_bst(self, values):
        if not values:
            return
        mid = len(values) // 2
        self.value = values[mid]
        left_values = values[:mid]
        right_values = values[mid+1:]
        
        if left_values:
            self.children[0] = TreeConverter(left_values[len(left_values) // 2], max_children=2)
            self.children[0]._build_bst(left_values)
        else:
            self.children[0] = None
        
        if right_values:
            self.children[1] = TreeConverter(right_values[len(right_values) // 2], max_children=2)
            self.children[1]._build_bst(right_values)
        else:
            self.children[1] = None

    def to_tst(self):
        values = self._extract_values()
        values = [v for v in values if v != 0]  # Remove 0 values
        values.sort()
        self._build_tst(values)
        return self

    def _extract_values(self):
        if self is None:
            return []
        values = []
        if isinstance(self, TreeConverter):
            for child in self.children:
                if child is not None:
                    if isinstance(child, TreeConverter):
                        values.extend(child._extract_values())
                    else:
                        values.append(child)
            values.append(self.value)
        return values

    def _build_tst(self, values):
        if not values:
            return
        mid = len(values) // 2
        self.value = values[mid]
        left_values = [v for v in values[:mid] if v < self.value]
        center_values = [v for v in values if v == self.value]
        right_values = [v for v in values[mid+1:] if v > self.value]

        if left_values:
            self.children[0] = TreeConverter(left_values[len(left_values) // 2], max_children=3)
            self.children[0]._build_tst(left_values)
        else:
            self.children[0] = None

        if len(center_values) > 1:
            self.children[1] = TreeConverter(center_values[len(center_values) // 2], max_children=3)
            self.children[1]._build_tst(center_values[len(center_values) // 2 + 1:])
        else:
            self.children[1] = None

        if right_values:
            self.children[2] = TreeConverter(right_values[len(right_values) // 2], max_children=3)
            self.children[2]._build_tst(right_values)
        else:
            self.children[2] = None
    
    def search(self, value):
        if self is None or self.value == 0:
            return False
        if self.value == value:
            return True
        if len(self.children) == 2:  # BST logic
            if value < self.value and self.children[0]:
                return self.children[0].search(value)
            elif value > self.value and self.children[1]:
                return self.children[1].search(value)
        elif len(self.children) == 3:  # TST logic
            if value < self.value and self.children[0]:
                return self.children[0].search(value)
            elif value > self.value and self.children[2]:
                return self.children[2].search(value)
            elif value == self.value and self.children[1]:
                return self.children[1].search(value)
        return False
    
    def visualize_networkx(self):
        G = nx.DiGraph()
        pos = {}
        self._build_networkx(self, G, pos, 0, 0, 1)
        plt.figure(figsize=(10, 8))
        nx.draw(G, pos, with_labels=True, labels=nx.get_node_attributes(G, 'label'), node_size=2000, node_color="skyblue", font_size=10, font_color="black", font_weight="bold", arrows=False)
        plt.show()

    def _build_networkx(self, node, G, pos, x, y, level):
        if node is None:
            return
        node_id = str(id(node))
        G.add_node(node_id, label=str(node.value))
        pos[node_id] = (x, y)
        
        x_offsets = [-1 + 2*i/(len(node.children)-1) for i in range(len(node.children))] if len(node.children) > 1 else [0]
        
        for i, child in enumerate(node.children):
            if child is not None and child != 0:
                child_id = str(id(child))
                G.add_edge(node_id, child_id)
                self._build_networkx(child, G, pos, x + x_offsets[i] / level, y - 1, level + 1)


