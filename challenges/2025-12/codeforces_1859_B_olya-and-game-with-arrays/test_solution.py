import pytest

# It's good practice to put the solution logic in a function,
# typically named `solve` or similar, to be easily testable.
def solve():
    """
    Reads input for one test case and prints the result.
    """
    n = int(input())
    
    overall_min = float('inf')
    sum