def main():
    n = int(input("Enter size of array: "))
    arr = []
    for i in range(n):
        arr.append(int(input(f"enter {i+1} element: ")))
    quick_sort(arr, 0, n-1)
    print(arr)
    
def quick_sort(a, low, high):
    if low < high:
        i = low
        j = high
        pivot = low
        
        while i < j:
            while i < len(a) and a[i] < a[pivot]:
                i += 1
            while a[j] > a[pivot]:
                j -= 1
            if i < j:
                a[i], a[j] = a[j], a[i]
        a[j], a[pivot] = a[pivot], a[j]   # placing the pivot in the correct position
        quick_sort(a, low, j-1) # left part
        quick_sort(a, j+1, high) #right part

if __name__ == '__main__':
    main()

