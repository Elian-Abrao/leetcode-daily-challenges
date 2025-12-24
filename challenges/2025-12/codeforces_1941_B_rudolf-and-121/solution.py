import sys

def solve():
    n = int(sys.stdin.readline())
    a = list(map(int, sys.stdin.readline().split()))

    # Iterate from the second element (index 1) up to the second to last element (index n-2).
    # This is because an operation at index `i` affects `a[i-1