class BinaryTreePrinter:
    def __init__(self, max_nodes):
        self.max_nodes = max_nodes
        self.tree_num = [0] * (max_nodes + 1)
        self.tree_num_sum = [0] * (max_nodes + 1)
        self._initialize()

    def _initialize(self):
        self.tree_num[0] = self.tree_num_sum[0] = 1
        for node_num in range(1, self.max_nodes + 1):
            self.tree_num[node_num] = 0
            for left_node_num in range(node_num):
                self.tree_num[node_num] += self.tree_num[left_node_num] * self.tree_num[node_num - 1 - left_node_num]
            self.tree_num_sum[node_num] = self.tree_num_sum[node_num - 1] + self.tree_num[node_num]

    def print_tree(self, order_num):
        if order_num == 0:
            return ""
        node_num = 1
        while self.tree_num_sum[node_num] <= order_num:
            node_num += 1
        return self._print_tree_helper(order_num - self.tree_num_sum[node_num - 1], node_num)

    def _print_tree_helper(self, order_num, node_num):
        if node_num == 0:
            return ""
        order_before = 0
        for left_node_num in range(node_num):
            if order_before + self.tree_num[left_node_num] * self.tree_num[node_num - 1 - left_node_num] > order_num:
                break
            order_before += self.tree_num[left_node_num] * self.tree_num[node_num - 1 - left_node_num]
        left_order_num = (order_num - order_before) // self.tree_num[node_num - 1 - left_node_num]
        right_order_num = (order_num - order_before) % self.tree_num[node_num - 1 - left_node_num]
        left_tree = self._print_tree_helper(left_order_num, left_node_num)
        right_tree = self._print_tree_helper(right_order_num, node_num - 1 - left_node_num)
        if left_tree:
            left_tree = f"({left_tree})"
        if right_tree:
            right_tree = f"({right_tree})"
        return f"{left_tree}X{right_tree}"