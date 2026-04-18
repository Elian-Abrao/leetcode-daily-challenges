class AllOne:
    class Bucket:
        __slots__ = ('count', 'keys', 'prev', 'next')
        def __init__(self, count: int):
            self.count = count
            self.keys = set()
            self.prev = None
            self.next = None

    def __init__(self):
        # Sentinel nodes to simplify insertions/removals at ends
        self.head = self.Bucket(0)   # left sentinel (count 0)
        self.tail = self.Bucket(-1)  # right sentinel
        self.head.next = self.tail
        self.tail.prev = self.head

        # Maps count -> bucket and key -> count
        self.count_to_bucket = {}  # int -> Bucket
        self.key_to_count = {}     # str -> int

    # Helper: insert new_bucket after node
    def _insert_after(self, node: 'AllOne.Bucket', new_bucket: 'AllOne.Bucket') -> None:
        nxt = node.next
        node.next = new_bucket
        new_bucket.prev = node
        new_bucket.next = nxt
        nxt.prev = new_bucket

    # Helper: insert new_bucket before node
    def _insert_before(self, node: 'AllOne.Bucket', new_bucket: 'AllOne.Bucket') -> None:
        prv = node.prev
        prv.next = new_bucket
        new_bucket.prev = prv
        new_bucket.next = node
        node.prev = new_bucket

    # Helper: remove bucket from the linked list
    def _remove_bucket(self, bucket: 'AllOne.Bucket') -> None:
        bucket.prev.next = bucket.next
        bucket.next.prev = bucket.prev
        bucket.prev = None
        bucket.next = None

    def inc(self, key: str) -> None:
        if key not in self.key_to_count:
            # New key: move to count 1
            new_count = 1
            bucket = self.count_to_bucket.get(1)
            if bucket is None:
                bucket = self.Bucket(1)
                self.count_to_bucket[1] = bucket
                self._insert_after(self.head, bucket)
            bucket.keys.add(key)
            self.key_to_count[key] = 1
        else:
            old_count = self.key_to_count[key]
            new_count = old_count + 1
            old_bucket = self.count_to_bucket[old_count]

            # Create new bucket for new_count if needed, place it after old_bucket
            new_bucket = self.count_to_bucket.get(new_count)
            if new_bucket is None:
                new_bucket = self.Bucket(new_count)
                self.count_to_bucket[new_count] = new_bucket
                self._insert_after(old_bucket, new_bucket)

            # Move key to new bucket
            new_bucket.keys.add(key)
            self.key_to_count[key] = new_count

            # Remove from old bucket
            old_bucket.keys.remove(key)
            if not old_bucket.keys:
                self._remove_bucket(old_bucket)
                del self.count_to_bucket[old_count]

    def dec(self, key: str) -> None:
        if key not in self.key_to_count:
            return  # As per problem statement, this should not happen
        count = self.key_to_count[key]
        old_bucket = self.count_to_bucket[count]
        new_count = count - 1

        if new_count == 0:
            # Remove key entirely
            old_bucket.keys.remove(key)
            del self.key_to_count[key]
            if not old_bucket.keys:
                self._remove_bucket(old_bucket)
                del self.count_to_bucket[count]
        else:
            # Ensure bucket for new_count exists, insert to the left of old_bucket
            new_bucket = self.count_to_bucket.get(new_count)
            if new_bucket is None:
                new_bucket = self.Bucket(new_count)
                self.count_to_bucket[new_count] = new_bucket
                self._insert_before(old_bucket, new_bucket)

            # Move key to new bucket
            new_bucket.keys.add(key)
            self.key_to_count[key] = new_count

            # Remove from old bucket
            old_bucket.keys.remove(key)
            if not old_bucket.keys:
                self._remove_bucket(old_bucket)
                del self.count_to_bucket[count]

    def getMaxKey(self) -> str:
        if self.head.next is self.tail:
            return ""
        max_bucket = self.tail.prev
        # Return any key from the max bucket
        return next(iter(max_bucket.keys))

    def getMinKey(self) -> str:
        if self.head.next is self.tail:
            return ""
        min_bucket = self.head.next
        return next(iter(min_bucket.keys))