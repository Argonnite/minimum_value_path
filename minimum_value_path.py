'''
Return root-to-leaf path containing minimum.  Ties broken by next minimum, and so on.

Ex.
   3
  / \
 4   9
  \  | \
   6 5  1
    /  / \
   1  8   4
  / \
 2   3

Return: 3, 9, 5, 1, 2

'''

class BinaryTreeNode(object):

    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

    def insert_left(self, value):
        self.left = BinaryTreeNode(value)

    def insert_right(self, value):
        self.right = BinaryTreeNode(value)


def return_min_path(node):
    q = []
    min_path = []

    q.append( (node, [node.value]) )  # prime DFS queue.

    while(len(q) > 0):
        current_node, current_values = q.pop()

        #if at terminus, check collected values
        if current_node.left == None and current_node.right == None:
            if len(min_path) == 0:
                min_path = current_values
            else:
                if sorted(current_values) < sorted(min_path):
                    min_path = current_values
        else:
            if current_node.left is not None:
                q.append( (current_node.left, current_values + [current_node.left.value]) )
            if current_node.right is not None:
                q.append( (current_node.right, current_values + [current_node.right.value]) )
    return min_path


root = BinaryTreeNode(3)
root.insert_left(4)
root.insert_right(9)
root.left.insert_right(6)
root.right.insert_left(5)
root.right.insert_right(1)
root.right.left.insert_left(1)
root.right.right.insert_left(8)
root.right.right.insert_right(4)
root.right.left.left.insert_left(2)
root.right.left.left.insert_right(3)

print(return_min_path(root))
