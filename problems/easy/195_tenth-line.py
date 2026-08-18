import sys

def solution():
    """
    Reads file.txt and prints the 10th line (1-indexed).
    If the file has fewer than 10 lines, prints nothing (empty output).
    This is a direct, efficient shell-style solution using only Python.
    """
    filename = "file.txt"
    line_count = 0
    target_line = 10
    
    try:
        with open(filename, "r") as f:
            for line in f:
                line_count += 1
                if line_count == target_line:
                    # Print the line without adding an extra newline
                    # (the line already contains its own trailing newline)
                    sys.stdout.write(line)
                    return  # Early exit once we find the target line
    except FileNotFoundError:
        # If file doesn't exist, output nothing (as required by problem)
        return
    
    # If we reached here, the file has fewer than 10 lines
    # Requirement: print nothing when line doesn't exist
    return

if __name__ == "__main__":
    solution()