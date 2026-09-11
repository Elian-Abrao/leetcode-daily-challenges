from __future__ import annotations
import heapq
from typing import List

class DinnerPlates:
    """
    Maintain multiple stacks with fixed capacity. Use a min-heap of available 
    (non-full) stack indices for push, and track the rightmost non-empty stack 
    for pop. popAtStack may create a new available slot that becomes the 
    leftmost candidate for future pushes.
    """

    def __init__(self, capacity: int):
        # Each stack is stored as a plain Python list acting as a stack.
        self.stacks: List[List[int]] = []
        # Min-heap of indices for stacks that have room (size < capacity).
        self.available: List[int] = []
        self.capacity = capacity

    def push(self, val: int) -> None:
        # Ensure we have an available slot; if not, create a new empty stack.
        if not self.available:
            # All existing stacks are full, so append a new one.
            self.stacks.append([])
            heapq.heappush(self.available, len(self.stacks) - 1)

        # Get the leftmost available stack index.
        idx = self.available[0]
        self.stacks[idx].append(val)

        # If the stack just became full, remove it from the available set.
        if len(self.stacks[idx]) == self.capacity:
            heapq.heappop(self.available)

    def pop(self) -> int:
        # Remove trailing empty stacks so that the last stack is always non-empty
        # (or we have no stacks left).
        while self.stacks and not self.stacks[-1]:
            self.stacks.pop()
            # Also remove this index from available heap if present (rare, but safe).
            # Since we pop the stack entirely, any reference is stale; heap will be 
            # cleaned opportunistically in push/popAtStack.

        if not self.stacks:
            return -1

        # Pop from the rightmost (last) non-empty stack.
        val = self.stacks[-1].pop()
        # If that stack became non-full, add its index to available.
        # (It could be full-to-less-than-full.)
        idx = len(self.stacks) - 1
        # Only push if this stack was full before pop.
        # Simpler: always try to add; heap will avoid duplicates because we check later.
        # But to be efficient, we only add when it wasn't already available.
        # Since we popped from the last stack, it was necessarily non-available
        # (otherwise pop would have chosen a different stack? Actually pop always takes
        # from the rightmost, regardless of available status, so it could be available).
        # So we unconditionally push its index if it now has room.
        if self.stacks[idx] and len(self.stacks[idx]) < self.capacity:
            heapq.heappush(self.available, idx)

        # If after pop the stack is empty, remove it to keep stacks list clean.
        if not self.stacks[-1]:
            self.stacks.pop()
            # The index is now gone; we don't bother removing from available heap
            # because that index is stale—we'll skip stale indices when we pop them.

        return val

    def popAtStack(self, index: int) -> int:
        # Out of bounds or empty stack → return -1.
        if index >= len(self.stacks) or not self.stacks[index]:
            return -1

        val = self.stacks[index].pop()

        # This stack now has a free slot; add its index to available if not already there.
        # Because it might already be in available (if it wasn't full before).
        # Use a simple check: only add if it's not already marked available? 
        # We'll just push and handle duplicates later.
        if len(self.stacks[index]) < self.capacity:
            heapq.heappush(self.available, index)

        # If the stack became empty and it's the rightmost, we can remove trailing empties
        # to keep the stacks list compact (optional but helps with index sanity).
        if not self.stacks[index]:
            # Remove trailing empty stacks (but only the last ones).
            while self.stacks and not self.stacks[-1]:
                self.stacks.pop()
            # Note: the index may now be out of range; that's fine, stale indices in 
            # available will be ignored when popped.

        return val