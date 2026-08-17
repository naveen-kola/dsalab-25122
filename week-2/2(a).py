def linear_search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return -1


arr = list(map(int, input("Enter the elements: ").split()))
key = int(input("Enter the element to search: "))

result = linear_search(arr, key)

if result != -1:
    print("Element found at position", result + 1)
else:
    print("Element not found")