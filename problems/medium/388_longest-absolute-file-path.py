class Solution:
    def lengthLongestPath(self, input: str) -> int:
        # Split the input by newline to get each file/directory entry.
        lines = input.split('\n')
        # Stack stores (depth, cumulative_length) for the current path.
        stack = []
        max_len = 0

        for line in lines:
            # Count leading tabs to determine depth.
            depth = len(line) - len(line.lstrip('\t'))
            # Name after removing leading tabs.
            name = line.lstrip('\t')

            # Pop entries from stack until we are at the correct parent depth.
            while stack and stack[-1][0] >= depth:
                stack.pop()

            # Compute cumulative length for this entry.
            if not stack:
                # Root level: no leading slash.
                cum_len = len(name)
            else:
                # Parent length + '/' + current name length.
                cum_len = stack[-1][1] + 1 + len(name)

            # Push current entry onto the stack.
            stack.append((depth, cum_len))

            # If the name contains a dot, it's a file; update max length.
            if '.' in name:
                max_len = max(max_len, cum_len)

        return max_len