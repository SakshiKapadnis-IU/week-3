
# Exercise 1: Fibonacci (Recursive)
def fibonacci(n):
    """
    Recursive function to return the nth Fibonacci number.
    """
    # Base cases
    if n == 0:
        return 0
    elif n == 1:
        return 1
    # Recursive case
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
    
