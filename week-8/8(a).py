class BinaryTreeArray:
    def __init__(self, size):
        self.tree = [None] * size
        self.size = size

    def insert(self, value, index):
        if index >= self.size:
            print("Index out of range")
        else:
            self.tree[index] = value

    def display(self):
        print("Binary Tree using Array:", self.tree)

    def search(self, value):
        if value in self.tree:
            print(value, "found in the tree")
        else:
            print(value, "not found in the tree")

    def delete(self, value):
        if value in self.tree:
            index = self.tree.index(value)
            self.tree[index] = None
            print(value, "deleted")
        else:
            print(value, "not found")


bt = BinaryTreeArray(7)

bt.insert(10, 0)
bt.insert(20, 1)
bt.insert(30, 2)
bt.insert(40, 3)
bt.insert(50, 4)

bt.display()
bt.search(20)
bt.delete(20)
bt.display()