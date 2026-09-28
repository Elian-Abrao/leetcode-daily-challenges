import heapq


class KthLargest:
    def __init__(self, k: int, nums: list[int]):
        self.k = k
        self.heap = list(nums)
        heapq.heapify(self.heap)

        # Keep only the k largest scores.
        # The minimum of this heap is exactly the kth largest score.
        while len(self.heap) > k:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        # If we have fewer than k scores, the heap is not full yet.
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)
        # Replace the current kth largest if the new score is larger.
        elif val > self.heap[0]:
            heapq.heapreplace(self.heap, val)

        # heap[0] is the smallest among the k largest scores seen so far.
        return self.heap[0]