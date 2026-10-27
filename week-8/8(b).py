class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTreeLinkedList:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)

        if self.root is None:
            self.root = new_node
            return

        queue = [self.root]

        while queue:
            current = queue.pop(0)

            if current.left is None:
                current.left = new_node
                return
            else:
                queue.append(current.left)

            if current.right is None:
                current.right = new_node
                return
            else:
                queue.append(current.right)

    def display(self, node):
        if node:
            print(node.data, end=" ")
            self.display(node.left)
            self.display(node.right)

    def search(self, node, value):
        if node is None:
            return False

        if node.data == value:
            return True

        return (self.search(node.left, value) or
                self.search(node.right, value))

    def delete(self, value):
        if self.root is None:
            print("Tree is empty")
            return

        queue = [(self.root, None)]
        target = None
        last = None
        parent_last = None

        while queue:
            current, parent = queue.pop(0)

            if current.data == value and target is None:
                target = current

            last = current
            parent_last = parent

            if current.left:
                queue.append((current.left, current))

            if current.right:
                queue.append((current.right, current))

        if target is None:
            print(value, "not found")
            return

        target.data = last.data

        if parent_last is None:
            self.root = None
        elif parent_last.right == last:
            parent_last.right = None
        else:
            parent_last.left = None

        print(value, "deleted")


bt = BinaryTreeLinkedList()

bt.insert(10)
bt.insert(20)
bt.insert(30)
bt.insert(40)
bt.insert(50)

print("Preorder Traversal:")
bt.display(bt.root)

print("\nSearch 20:", bt.search(bt.root, 20))

bt.delete(20)

print("After deletion:")
bt.display(bt.root)
print()