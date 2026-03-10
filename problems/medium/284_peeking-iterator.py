class PeekingIterator:
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.iterator = iterator
        self._has_next = iterator.hasNext()
        self._next_value = iterator.next() if self._has_next else None

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        return self._next_value

    def next(self):
        """
        :rtype: int
        """
        current = self._next_value
        self._has_next = self.iterator.hasNext()
        self._next_value = self.iterator.next() if self._has_next else None
        return current

    def hasNext(self):
        """
        :rtype: bool
        """
        return self._has_next


class Solution:
    PeekingIterator = PeekingIterator