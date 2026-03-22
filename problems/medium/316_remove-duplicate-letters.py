class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        # Last position of each character tells us whether it is safe to remove
        # a character now and pick it again later.
        last_index = {ch: i for i, ch in enumerate(s)}

        stack = []
        in_stack = set()

        for i, ch in enumerate(s):
            # Skip duplicates already chosen; every letter must appear once.
            if ch in in_stack:
                continue

            # Maintain the smallest lexicographical stack possible.
            # We can remove a larger top character if it appears again later,
            # because keeping the smaller current character earlier is better.
            while stack and ch < stack[-1] and last_index[stack[-1]] > i:
                removed = stack.pop()
                in_stack.remove(removed)

            stack.append(ch)
            in_stack.add(ch)

        # Stack already stores the answer in order.
        return "".join(stack)