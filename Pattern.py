def lower_triangular(n):
    for i in range(1, n+1):
        print('*' * i)

def upper_triangular(n):
    for i in range(n):
        print(' ' * i + '*' * (n - i))

def pyramid(n):
    for i in range(n):
        print(' ' * (n - i - 1) + '*' * (2 * i + 1))

# Example usage
size=int(input("\nEnter the number rows :"))
print("Lower Triangular:")
lower_triangular(size)
print("\nUpper Triangular:")
upper_triangular(size)
print("\nPyramid:")
pyramid(size)
