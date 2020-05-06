class Node:
    def __init__(self, val):
        self.val = val



class BinaryTreeNode(Node):
    def __init__(self, val):
        super().__init__(val)
        self.left = None
        self.right = None

    def __str__(self):
        '''
            Will output as such when printed

             [5]
            /	\
          [3]	[8]
        '''

        left_node_val = self.left.val if self.left else None
        right_node_val = self.right.val if self.right else None

        return f'\t [{self.val}]   \n\t/\t\ \n  [{left_node_val}]\t[{right_node_val}]\n'



class LinkedListNode(Node):
    def __init__(self, val):
        super().__init__(val)
        self.next = None

    def __str__(self):
        '''
            Will output as such when printed

            [5] --> [8]

        '''

        next_node_val = self.next.val if self.next else None

        return f'[{self.val}] --> [{next_node_val}]\n'



class JumpListNode(LinkedListNode):
    def __init__(self, val):
        super().__init__(val)
        self.jump = None
        self.order = None

    def __str__(self):
        '''
            Will output as such when printed

            [5] --> [8]
             \
              -----> [99]
        '''

        next_node_val = self.next.val if self.next else None
        jump_node_val = self.jump.val if self.jump else None

        return f'[{self.val}] --> [{next_node_val}]\n \\ \n  -----> [{jump_node_val}]\n'
