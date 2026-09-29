class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = -1
        self.rear = -1

    # Enqueue operation
    def enqueue(self, data):
        if (self.rear + 1) % self.size == self.front:
            print("Queue Overflow")
            return

        if self.front == -1:
            self.front = 0

        self.rear = (self.rear + 1) % self.size
        self.queue[self.rear] = data
        print("Element inserted successfully")

    # Dequeue operation
    def dequeue(self):
        if self.front == -1:
            print("Queue Underflow")
            return

        print("Deleted element:", self.queue[self.front])

        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.size

    # Peek operation
    def peek(self):
        if self.front == -1:
            print("Queue is empty")
        else:
            print("Front element:", self.queue[self.front])

    # Display operation
    def display(self):
        if self.front == -1:
            print("Queue is empty")
            return

        print("Queue elements:")
        i = self.front

        while True:
            print(self.queue[i], end=" ")
            if i == self.rear:
                break
            i = (i + 1) % self.size

        print()


def main():
    size = int(input("Enter queue size: "))
    q = CircularQueue(size)

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