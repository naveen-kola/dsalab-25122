class Stack:
    def __init__(self):
        self.stack = []

    # Push operation
    def push(self, data):
        self.stack.append(data)
        print("Element pushed successfully")

    # Pop operation
    def pop(self):
        if len(self.stack) == 0:
            print("Stack Underflow")
        else:
            print("Popped element:", self.stack.pop())

    # Peek operation
    def peek(self):
        if len(self.stack) == 0:
            print("Stack is empty")
        else:
            print("Top element:", self.stack[-1])

    # Display operation
    def display(self):
        if len(self.stack) == 0:
            print("Stack is empty")
        else:
            print("Stack elements:")
            for i in range(len(self.stack) - 1, -1, -1):
                print(self.stack[i])


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