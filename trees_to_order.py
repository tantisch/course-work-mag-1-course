NODE_NUM_MAX = 18
tree_num = [0] * (NODE_NUM_MAX + 1) # Кількість можливих піддерев З якоюсь кількістю ноудів
tree_num_sum = [0] * (NODE_NUM_MAX + 1) # Сумарна кількість всіх піддерев ДО (включно) якоїсь кількості ноудів

def initialize():
    tree_num[0] = tree_num_sum[0] = 1
    for node_num in range(1, NODE_NUM_MAX + 1):
        tree_num[node_num] = 0
        for left_node_num in range(node_num):
            tree_num[node_num] += tree_num[left_node_num] * tree_num[node_num - 1 - left_node_num]
        tree_num_sum[node_num] = tree_num_sum[node_num - 1] + tree_num[node_num]

def print_tree(order_num, node_num):
    if node_num == 0:
        return

    order_before = 0   

    '''
    left_node_num - Кількість ноудів у лівому піддереві нашого дерева з order_num (node_num - 1 - left_node_num - у правому піддереві)
    order_before - Кількість дерев з кількістю ноудів node_num, але у яких кількість ноудів у лівих піддереваї менша за left_node_num (менша ніж у нашого дерева)
    '''
    for left_node_num in range(node_num):  
        if order_before + tree_num[left_node_num] * tree_num[node_num - 1 - left_node_num] > order_num:
            break
        order_before += tree_num[left_node_num] * tree_num[node_num - 1 - left_node_num]

    ''' 
    Приклад:
    Дерево під номеров 20:
    node_num: 4
    order_num: 11 - порядоковий номер дерева для дерев з 4 ноудами
    left_node_num: 3 
    order_before: 9 - існує 9 дерев з кількістю ноудів node_num, але з меншою кількістю ноудів у лівому піддереві ніж 3
    order_num - order_before: 11 - 9 = 2 - на якому місці знаходиться наше дерево з кількістю ноудів node_num та кількістю ноудів у лівому підддереві left_node_num
    N_R = tree_num[node_num - 1 - left_node_num]: 0 - кількість можливих правих піддерев (4 - 1 - 3 = 0)
    
    Уявимо таблицю де:
        -Рядки матриці відповідають різним можливим деревам для лівого піддерева
        -Стовпці матриці відповідають різним можливим деревам для правого піддерева
    (order_num - order_before) // tree_num[node_num - 1 - left_node_num]: 2 // 0  = 2 - вказує номер рядка, який є індексом конкретного лівого піддерева. 
                                                                                        Це тому, що кожен "рядок" у нашій матриці містить N_R елементів, 
                                                                                        і відповідає одному унікальному лівому піддереву.
    (order_num - order_before) % tree_num[node_num - 1 - left_node_num]: 2 % 0 = 0 - аналогічно ряхує номер "cтовпця", який є індексом правого піддерева.
    '''
    left_order_num = (order_num - order_before) // tree_num[node_num - 1 - left_node_num] 
    right_order_num = (order_num - order_before) % tree_num[node_num - 1 - left_node_num] 
    
    if left_node_num != 0:
        print("(", end="")
        print_tree(left_order_num, left_node_num)
        print(")", end="")
    print("X", end="")
    if node_num - 1 - left_node_num != 0:
        print("(", end="")
        print_tree(right_order_num, node_num - 1 - left_node_num)
        print(")", end="")

if __name__ == "__main__":
    initialize()
    while True:
        order_num = int(input())
        if order_num == 0:
            break
        node_num = 1
        while tree_num_sum[node_num] <= order_num:
            node_num += 1
        print_tree(order_num - tree_num_sum[node_num - 1], node_num)
        print()

