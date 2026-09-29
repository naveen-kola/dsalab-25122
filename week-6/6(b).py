class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    # Push operation
    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
        print("Element pushed successfully")

    # Pop operation
    def pop(self):
        if self.top is None:
            print("Stack Underflow")
        else:
            print("Popped element:", self.top.data)
            self.top = self.top.next

    # Peek operation
    def peek(self):
        if self.top is None:
            print("Stack is empty")
        else:
            print("Top element:", self.top.data)

    # Display operation
    def display(self):
        if self.top is None:
            print("Stack is empty")
        else:
            temp = self.top
            print("Stack elements:")
            while temp:
                print(temp.data)
                temp = temp.next


def main():
    s = Stack()

    while True:
        print("\n1. Push")
        print("2. Pop")
        print("3. Peek")
        print("4. Display")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            data = int(input("Enter the element: "))
            s.push(data)

        elif choice == "2":
            s.pop()

        elif choice == "3":
            s.peek()

        elif choice == "4":
            s.display()

        elif choice == "5":
            print("Exiting the program")
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()