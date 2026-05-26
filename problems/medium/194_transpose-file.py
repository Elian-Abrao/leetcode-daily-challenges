#!/usr/bin/env python3
import sys

def main():
    # Read all lines from stdin
    lines = []
    for line in sys.stdin:
        # Strip newline but preserve structure
        lines.append(line.rstrip('\n'))
    
    # Handle edge case: empty file
    if not lines:
        return
    
    # Split each line into columns
    rows = [line.split(' ') for line in lines]
    
    # Handle edge case: single row (just print it as is)
    if len(rows) == 1:
        print(' '.join(rows[0]))
        return
    
    # Determine number of columns (assuming all rows have same number)
    num_cols = len(rows[0]) if rows else 0
    
    # Transpose: iterate through columns, collecting elements from each row
    for col_idx in range(num_cols):
        transposed_row = []
        for row in rows:
            transposed_row.append(row[col_idx])
        print(' '.join(transposed_row))

if __name__ == '__main__':
    main()