from data_structures.node import JumpListNode



def jump_order_traversal(head):
    global_counter = [1]

    _jump_order_traversal(head, global_counter)



def _jump_order_traversal(head, counter):
    if not head or head.order != -1:
        return

    head.order = counter[0]
    print('[{}] -> [{}]'.format(counter[0], head.val))

    counter[0] += 1

    _jump_order_traversal(head.jump, counter)
    _jump_order_traversal(head.next, counter)



def jump_order_traversal_iterative(head):
    stack = []
    stack.append(head)

    counter = 1

    while stack:
        curr_node = stack.pop()

        if not curr_node or curr_node.order != -1:
            continue

        print('[{}] -> [{}]'.format(counter, curr_node.val))
        curr_node.order = counter

        counter += 1

        stack.append(curr_node.next)
        stack.append(curr_node.jump)



def run_example():
    a = JumpListNode('a')
    b = JumpListNode('b')
    c = JumpListNode('c')
    d = JumpListNode('d')

    a.next = b
    a.jump = b

    b.next = c
    b.jump = d

    c.next = d

    jump_order_traversal(a)

    '''
    [1] -> [a]
    [2] -> [b]
    [3] -> [d]
    [4] -> [c]
    '''


if __name__ == '__main__':
    run_example()
