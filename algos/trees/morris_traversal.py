from data_structures.node import BinaryTreeNode

def in_order_constant_space(root):
    temp = root

    while temp:
        if not temp.left:
            print(temp.val, end=' ')
            temp = temp.right
        else:
            left_subtree = temp.left
            temp.left = None

            in_order_parent = find_in_order_parent(left_subtree)
            in_order_parent.right = temp

            temp = left_subtree


def find_in_order_parent(subtree):
    in_order_parent = subtree
    while in_order_parent.right:
        in_order_parent = in_order_parent.right

    return in_order_parent


def run_example():
    '''
                 6
            4           7
        3      5    6.3
    2
    '''

    root = BinaryTreeNode(6)
    root.left = BinaryTreeNode(4)
    root.left.left = BinaryTreeNode(3)
    root.left.left.left = BinaryTreeNode(2)
    root.left.right = BinaryTreeNode(5)
    root.right = BinaryTreeNode(7)
    root.right.left = BinaryTreeNode(6.3)

    # 2 3 4 5 6 6.3 7 
    in_order_constant_space(root)





if __name__ == '__main__':
    run_example()
