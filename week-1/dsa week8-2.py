class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__ (self):
        self.root = None

    def create_tree(self):
        self.root = Node('A')

        self.root.left = Node('B')
        self.roor.right = Node('C')

        self.root.left.left = Node('E')
        self.root.left.right = Node('F')

        self.root.right.right = Node('G')

    def preorder(self,node):

        if node is None:
            return
        print(node.data, end="")

        self.preorder(node.left)
        self.preorder(node.right)

    def inorder(self,node):

        if node is None:
            return

        self.inorder(node.left)
        print(node.data, end="")

    def postorder(self,node):

        if node is Node:
            return

        self.postorder(node.left)
        self.postorder(node.right)

        print(node.data, end="")

    def level_order(self):
        if self.root is None:
            return

        queue = [self.root]

        while queue:
            node = queue.pop(0)

            print(node.data
            

        


        
