class Queue:
    def __init__(self):
        self.queue = []

    # Enqueue operation
    def enqueue(self, data):
        self.queue.append(data)
        print("Element inserted successfully")

    # Dequeue operation
    def dequeue(self):
        if len(self.queue) == 0:
            print("Queue Underflow")
        else:
            print("Deleted element:", self.queue.pop(0))

    # Peek operation
    def peek(self):
        if len(self.queue) == 0:
            print("Queue is empty")
        else:
            print("Front element:", self.queue[0])

    # Display operation
    def display(self):
        if len(self.queue) == 0:
            print("Queue is empty")
        else:
            print("Queue elements:", self.queue)


def main():
    q = Queue()

    while True:
        print("\n1. Enqueue")
        print("2. Dequeue")
        print("3. Peek")
        print("4. Display")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            data = int(input("Enter the element: "))
            q.enqueue(data)

        elif choice == "2":
            q.dequeue()

        elif choice == "3":
            q.peek()

        elif choice == "4":
            q.display()

        elif choice == "5":
            print("Exiting the program")
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()