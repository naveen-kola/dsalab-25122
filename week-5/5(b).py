class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    # Insert at beginning
    def insert_begin(self, data):
        new_node = Node(data)

        if self.head is not None:
            new_node.next = self.head
            self.head.prev = new_node

        self.head = new_node

    # Insert at end
    def insert_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = new_node
        new_node.prev = temp

    # Insert at index (0-based)
    def insert_index(self, data, index):
        if index < 0 or index > self.size():
            print("Invalid index")
            return

        if index == 0:
            self.insert_begin(data)
            return

        new_node = Node(data)
        temp = self.head

        for i in range(index - 1):
            temp = temp.next

        new_node.next = temp.next
        new_node.prev = temp

        if temp.next:
            temp.next.prev = new_node

        temp.next = new_node

    # Delete by value
    def delete_value(self, value):
        temp = self.head

        while temp and temp.data != value:
            temp = temp.next

        if temp is None:
            print("Value not found")
            return

        if temp.prev:
            temp.prev.next = temp.next
        else:
            self.head = temp.next

        if temp.next:
            temp.next.prev = temp.prev

        print("Node deleted successfully")

    # Delete prior node (before a given value)
    def delete_prior(self, value):
        temp = self.head

        while temp and temp.data != value:
            temp = temp.next

        if temp is None:
            print("Value not found")
            return

        if temp.prev is None:
            print("No prior node exists")
            return

        node = temp.prev

        if node.prev:
            node.prev.next = temp
        else:
            self.head = temp

        temp.prev = node.prev
        print("Prior node deleted successfully")

    # Delete last node
    def delete_last(self):
        if self.head is None:
            print("Linked list is empty")
            return

        temp = self.head

        if temp.next is None:
            self.head = None
            return

        while temp.next:
            temp = temp.next

        temp.prev.next = None
        print("Last node deleted successfully")

    # Count nodes
    def size(self):
        count = 0
        temp = self.head

        while temp:
            count += 1
            temp = temp.next

        return count

    # Display list
    def display(self):
        if self.head is None:
            print("Linked list is empty")
            return

        temp = self.head

        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.next

        print("None")


def main():
    my_list = None

    while True:
        print("\n1. Create LL")
        print("2. Insert at Beginning")
        print("3. Insert at End")
        print("4. Insert at Index")
        print("5. Delete by Value")
        print("6. Delete Prior Node")
        print("7. Delete Last Node")
        print("8. Count Number of Nodes")
        print("9. Display/Traverse")
        print("10. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            my_list = DoublyLinkedList()
            print("Linked list created successfully")

        elif choice == "2":
            if my_list is None:
                print("Please create the linked list first")
            else:
                data = int(input("Enter data: "))
                my_list.insert_begin(data)
                print("Element inserted")

        elif choice == "3":
            if my_list is None:
                print("Please create the linked list first")
            else:
                data = int(input("Enter data: "))
                my_list.insert_end(data)
                print("Element inserted")

        elif choice == "4":
            if my_list is None:
                print("Please create the linked list first")
            else:
                data = int(input("Enter data: "))
                index = int(input("Enter index (starting from 0): "))
                my_list.insert_index(data, index)

        elif choice == "5":
            if my_list is None:
                print("Please create the linked list first")
            else:
                value = int(input("Enter value to delete: "))
                my_list.delete_value(value)

        elif choice == "6":
            if my_list is None:
                print("Please create the linked list first")
            else:
                value = int(input("Enter value: "))
                my_list.delete_prior(value)

        elif choice == "7":
            if my_list is None:
                print("Please create the linked list first")
            else:
                my_list.delete_last()

        elif choice == "8":
            if my_list is None:
                print("Please create the linked list first")
            else:
                print("Number of nodes:", my_list.size())

        elif choice == "9":
            if my_list is None:
                print("Please create the linked list first")
            else:
                my_list.display()

        elif choice == "10":
            print("Exiting the program")
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()