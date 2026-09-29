def main():
    n = int(input("Enter size of array: "))
    arr = []
    for i in range(n):
        arr.append(input(f"enter {i+1} element: "))
    sorted_arr = merge_sort(arr)
    print(sorted_arr)
    
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)
    
def merge(left, right):
    arr = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j] :
            arr.append(left[i])
            i += 1
        else:
            arr.append(right[j])
            j += 1
    arr.extend(left[i:])
    arr.extend(right[j:])
    return arr

if __name__ == '__main__':
    main()
