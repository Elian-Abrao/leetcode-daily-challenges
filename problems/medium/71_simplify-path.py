class Solution:
    def simplifyPath(self, path: str) -> str:
        """
        Simplify an absolute Unix-style path.

        Approach:
        - Split the path by '/' to obtain path components.
        - Use a stack to build the canonical path:
          - Ignore empty components and '.' (current dir).
          - For '..', pop from stack if possible (move to parent).
          - Otherwise, push the valid directory/file name onto the stack.
        - Join stack with '/' and prefix with a leading '/'.
        - If stack is empty, return root "/".
        """
        # Split path into components; consecutive slashes yield empty strings.
        components = path.split('/')

        stack = []
        for comp in components:
            if comp == '' or comp == '.':
                # Ignore empty segments and current directory references.
                continue
            if comp == '..':
                # Move to parent directory if possible.
                if stack:
                    stack.pop()
            else:
                # Valid directory or file name; keep it.
                stack.append(comp)

        # Build the canonical path.
        canonical = '/' + '/'.join(stack)
        return canonical