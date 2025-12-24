import sys

def solve():
    n = int(sys.stdin.readline())
    
    # Store all minimums from each array
    all_min_elements = []
    
    # Store all second minimums from each array (or the minimum if array has only one element)
    # This will be used to find the global minimum among all arrays' minimums.