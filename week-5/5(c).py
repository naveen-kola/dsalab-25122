class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    # Insert at beginning
    def insert_begin(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            new_node.next = self.head
            return

        temp = self.head
        while temp.next != self.head:
            temp = temp.next

        new_node.next = self.head
        temp.next = new_node
        self.head = new_node

    # Insert at end
    def insert_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            new_node.next = self.head
            return

        temp = self.head
        while temp.next != self.head:
            temp = temp.next

        temp.next = new_node
        new_node.next = self.head

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
        temp.next = new_node

    # Delete by value
    def delete_value(self, value):
        if self.head is None:
            print("Linked list is empty")
            return

        temp = self.head
        prev = None

        while True:
            if temp.data == value:
                break
            prev = temp
            temp = temp.next
            if temp == self.head:
                print("Value not found")
                return

        if temp == self.head:
            if self.head.next == self.head:
                self.head = None
                return

            last = self.head
            while last.next != self.head:
                last = last.next

            self.head = self.head.next
            last.next = self.head
        else:
            prev.next = temp.next

        print("Node deleted successfully")

    # Delete prior node (before a given value)
    def delete_prior(self, value):
        if self.head is None or self.head.next == self.head:
            print("No prior node exists")
            return

        temp = self.head
        prev = None

        while temp.data != value:
            prev = temp
            temp = temp.next
            if temp == self.head:
                print("Value not found")
                return

        if temp == self.head:
            last = self.head
            while last.next.next != self.head:
                last = last.next

            last.next = self.head
            print("Prior node deleted successfully")
            return

        if temp == self.head.next:
            last = self.head
            while last.next != self.head:
                last = last.next

            self.head = temp
            last.next = self.head
            print("Prior node deleted successfully")
            return

        node = self.head
        while node.next != temp:
            node = node.next

        prev_node = self.head
        while prev_node.next != node:
            prev_node = prev_node.next

        prev_node.next = temp
        print("Prior node deleted successfully")

    # Delete last node
    def delete_last(self):
        if self.head is None:
            print("Linked list is empty")
            return

        if self.head.next == self.head:
            self.head = None
            print("Last node deleted successfully")
            return

        temp = self.head
        while temp.next.next != self.head:
            temp = temp.next

        temp.next = self.head
        print("Last node deleted successfully")

    # Count nodes
    def size(self):
        if self.head is None:
            return 0

        count = 1
        temp = self.head

        while temp.next != self.head:
            count += 1
            temp = temp.next

        return count

    # Display list
    def display(self):
        if self.head is None:
            print("Linked list is empty")
            return

        temp = self.head

        while True:
            print(temp.data, end=" -> ")
            temp = temp.next
            if temp == self.head:
                break

        print("(Back to Head)")


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
            my_list = CircularLinkedList()
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