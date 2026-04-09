class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # Empty list is the only trivial case; return early to avoid extra checks later.
        if head is None:
            return None

        current = head

        # Pass 1: insert each cloned node right after its original node.
        # This interleaving lets us find "original -> clone" in O(1) without a hash map.
        while current:
            copied = Node(current.val, current.next, None)
            current.next = copied
            current = copied.next

        current = head

        # Pass 2: wire random pointers for clones.
        # If original.random exists, its clone is original.random.next by construction.
        while current:
            copied = current.next
            if current.random is not None:
                copied.random = current.random.next
            current = copied.next

        # Pass 3: detach the interleaved list into original and copied lists.
        copied_head = head.next
        current = head

        while current:
            copied = current.next
            next_original = copied.next

            # Restore the original list structure.
            current.next = next_original

            # Link the copied list, skipping over originals.
            if next_original is not None:
                copied.next = next_original.next

            current = next_original

        return copied_head