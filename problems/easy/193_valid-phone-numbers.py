# This problem requires a bash one-liner, not Python code.
# The solution is a bash script using grep with regex:

# grep -E '^([0-9]{3}-|\([0-9]{3}\) )[0-9]{3}-[0-9]{4}$' file.txt

# Explanation:
# - grep -E enables extended regex
# - ^ anchors to start of line
# - ([0-9]{3}-|\([0-9]{3}\) ) matches either:
#   - Three digits followed by hyphen: 123-
#   - OR opening paren, three digits, closing paren, space: (123) 
# - [0-9]{3}-[0-9]{4} matches the remaining format: 456-7890
# - $ anchors to end of line

# Since this is a shell scripting problem with metadata {"shell": true},
# Python code is not applicable. However, to satisfy the template requirement
# of returning valid Python code, here's a Python equivalent that would work
# if this were adapted to a Python problem:

import re
import sys

def validate_phone_numbers(filename):
    # Regex pattern matching both valid formats
    pattern = r'^([0-9]{3}-|\([0-9]{3}\) )[0-9]{3}-[0-9]{4}$'
    
    try:
        with open(filename, 'r') as f:
            for line in f:
                # Strip newline but preserve format (no leading/trailing spaces per problem)
                line = line.rstrip('\n')
                if re.match(pattern, line):
                    print(line)
    except FileNotFoundError:
        pass

# For LeetCode shell problems, this Python code won't be executed
# The actual solution is the bash command above