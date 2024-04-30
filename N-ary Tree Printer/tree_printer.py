from itertools import product

def get_children_combinations(N, m):
    combinations = list(product(range(N), repeat=m))
    valid_combinations = [comb for comb in combinations if sum(comb) == N - 1]
    return valid_combinations

def get_indices(linear_index, dimensions):
    indices = []
    current_index = linear_index
    for dimension in reversed(dimensions):
        indices.append(current_index % dimension)
        current_index //= dimension
    indices.reverse()  # Reverse to start from the first dimension
    return indices

    

class TreePrinter:
    def __init__(self, max_children, max_nodes):
        self.max_nodes = max_nodes
        self.max_children = max_children
        self.tree_num = [0] * (max_nodes + 1)
        self.tree_num_sum = [0] * (max_nodes + 1)
        self.children_combinations = [None]
        self._initialize()

    # for example if children_node_nums == (3, 1, 2) the left subtree as 3 nodes, center has 1 node and right has 2 nodes
    # this function calculates all possitlbe trees with these children number of nodes
    def get_tree_num_product(self, children_node_nums):
        tree_num_product = 1
        for child_node_num in children_node_nums:
            tree_num_product *= self.tree_num[child_node_num]
        return tree_num_product

    def _initialize(self):
        self.tree_num[0] = self.tree_num_sum[0] = 1
        for node_num in range(1, self.max_nodes + 1):
            self.tree_num[node_num] = 0
            children_combs = get_children_combinations(node_num, self.max_children)
            self.children_combinations.append(children_combs)
            for children_node_nums in children_combs:
                tree_num_product = self.get_tree_num_product(children_node_nums)
                self.tree_num[node_num] += tree_num_product
            self.tree_num_sum[node_num] = self.tree_num_sum[node_num - 1] + self.tree_num[node_num]

    def print_tree(self, order_num):
        if order_num == 0:
            return ""
        node_num = 1
        while self.tree_num_sum[node_num] <= order_num:
            node_num += 1
        return self.print_tree_helper(order_num - self.tree_num_sum[node_num - 1], node_num)
    
    def print_tree_helper(self, order_num, node_num):
        if node_num == 0:
            return ''
        order_before = 0 
        for children_node_nums in self.children_combinations[node_num]:
            tree_num_product = self.get_tree_num_product(children_node_nums)
            if order_before + tree_num_product > order_num:
                break
            order_before += tree_num_product

        dimensions = [self.tree_num[child_node_num] for child_node_num in children_node_nums]
        
        children_order_nums = get_indices(order_num - order_before, dimensions)
        children_trees = [self.print_tree_helper(children_order_nums[child], children_node_nums[child]) for child in range(self.max_children)]

        output = 'X('
        for ind, child_tree in enumerate(children_trees):
            if child_tree:
                if ind > 0: 
                    output += ','
                children_trees[ind] = f'({child_tree})'
                output += f'({child_tree})'
            else:
                if ind > 0: 
                    output += ','
                output += '0'
        output += ')'

        return output

