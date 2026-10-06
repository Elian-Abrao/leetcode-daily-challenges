class Solution:
    def removeComments(self, source: list[str]) -> list[str]:
        """
        Removes line comments ('//') and block comments ('/* ... */') from a C++ source.
        The result lines are returned, omitting any line that becomes empty.
        """
        result = []
        in_block = False          # True when inside a block comment (/* ... */)
        current_line = []         # characters of the line being built

        for line in source:
            i = 0
            n = len(line)

            while i < n:
                if not in_block:
                    # Check for line comment "//"
                    if i + 1 < n and line[i] == '/' and line[i+1] == '/':
                        # Ignore the rest of this line
                        break
                    # Check for block comment start "/*"
                    if i + 1 < n and line[i] == '/' and line[i+1] == '*':
                        in_block = True
                        i += 2
                        continue
                    # Normal character – add to output
                    current_line.append(line[i])
                    i += 1
                else:
                    # Inside block comment – look for closing "*/"
                    if i + 1 < n and line[i] == '*' and line[i+1] == '/':
                        in_block = False
                        i += 2
                        continue
                    # All other characters inside block comment are ignored
                    i += 1

            # After processing a line, if we are NOT inside a block comment
            # and we have collected some characters, add that line to output.
            if not in_block and current_line:
                result.append(''.join(current_line))
                current_line = []   # reset for next line

        # Empty lines have been automatically omitted
        return result