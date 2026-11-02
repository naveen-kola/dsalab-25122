
# cse25122 Naveen 

size = 10

# Separate Chaining
class SeparateChaining:
    def __init__(self):
        self.table = [[] for i in range(size)]

    def insert(self, key):
        index = key % size
        if key not in self.table[index]:
            self.table[index].append(key)

    def search(self, key):
        index = key % size
        return key in self.table[index]

    def display(self):
        for i in range(size):
            print(i, ":", self.table[i])


# Linear Probing
class LinearProbing:
    def __init__(self):
        self.table = [None] * size

    def insert(self, key):
        index = key % size

        for i in range(size):
            new_index = (index + i) % size
            if self.table[new_index] is None:
                self.table[new_index] = key
                return

        print("Hash table is full!")

    def search(self, key):
        index = key % size

        for i in range(size):
            new_index = (index + i) % size

            if self.table[new_index] is None:
                return False

            if self.table[new_index] == key:
                return True

        return False

    def display(self):
        for i in range(size):
            print(i, ":", self.table[i])


# Quadratic Probing
class QuadraticProbing:
    def __init__(self):
        self.table = [None] * size

    def insert(self, key):
        index = key % size

        for i in range(size):
            new_index = (index + i * i) % size

            if self.table[new_index] is None:
                self.table[new_index] = key
                return

        print("No empty position found!")

    def search(self, key):
        index = key % size

        for i in range(size):
            new_index = (index + i * i) % size

            if self.table[new_index] is None:
                return False

            if self.table[new_index] == key:
                return True

        return False

    def display(self):
        for i in range(size):
            print(i, ":", self.table[i])


# Main Program
while True:
    print("\n--- HASHING OPERATIONS ---")
    print("1. Separate Chaining")
    print("2. Linear Probing")
    print("3. Quadratic Probing")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 4:
        print("Exiting...")
        break

    if choice == 1:
        h = SeparateChaining()
    elif choice == 2:
        h = LinearProbing()
    elif choice == 3:
        h = QuadraticProbing()
    else:
        print("Invalid choice!")
        continue

    while True:
        print("\n1. Insert")
        print("2. Search")
        print("3. Display")
        print("4. Back to Main Menu")

        op = int(input("Enter operation: "))

        if op == 1:
            key = int(input("Enter key: "))
            h.insert(key)

        elif op == 2:
            key = int(input("Enter key: "))
            if h.search(key):
                print("Key found!")
            else:
                print("Key not found!")

        elif op == 3:
            print("Hash Table:")
            h.display()

        elif op == 4:
            break

        else:
            print("Invalid operation!")
