def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


n = int(input("Enter the number of terms: "))

if n <= 0:
    print("Enter a positive number")
else:
    for i in range(n):
        print(fibonacci(i), end=" ")