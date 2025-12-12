# Recursive factorial function
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

print("Factorial of 6:", factorial(6))
