# Circular Queue using Linked List

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularQueue:
    def __init__(self):
        self.front = None
        self.rear = None

    # Enqueue operation
    def enqueue(self, data):
        new_node = Node(data)

        if self.front is None:
            self.front = new_node
            self.rear = new_node
            new_node.next = self.front
        else:
            new_node.next = self.front
            self.rear.next = new_node
            self.rear = new_node

        print(data, "inserted into the queue")

    # Dequeue operation
    def dequeue(self):
        if self.front is None:
            print("Queue is Empty")
            return

        value = self.front.data

        if self.front == self.rear:
            self.front = None
            self.rear = None
        else:
            self.front = self.front.next
            self.rear.next = self.front

        print(value, "deleted from the queue")

    # Peek operation
    def peek(self):
        if self.front is None:
            print("Queue is Empty")
        else:
            print("Front element:", self.front.data)

    # Display operation
    def display(self):
        if self.front is None:
            print("Queue is Empty")
            return

        print("Circular Queue elements:")

        temp = self.front

        while True:
            print(temp.data, end=" ")

            temp = temp.next

            if temp == self.front:
                break

        print()


# Main program
cq = CircularQueue()

while True:
    print("\n----- CIRCULAR QUEUE MENU -----")
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Peek")
    print("4. Display")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        value = int(input("Enter the element: "))
        cq.enqueue(value)

    elif choice == 2:
        cq.dequeue()

    elif choice == 3:
        cq.peek()

    elif choice == 4:
        cq.display()

    elif choice == 5:
        print("Exiting program...")
        break

    else:
        print("Invalid choice! Please try again.")