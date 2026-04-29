import heapq

class MedianFinder:
    def __init__(self):
        # Max heap for the smaller half (store negatives to simulate max heap)
        # Invariant: all elements in max_heap <= all elements in min_heap
        self.max_heap = []
        
        # Min heap for the larger half
        self.min_heap = []
        
        # Maintain size balance: len(max_heap) == len(min_heap) or len(max_heap) == len(min_heap) + 1

    def addNum(self, num: int) -> None:
        # Strategy: always add to max_heap first, then balance
        # This ensures max_heap contains the smaller half
        
        # If max_heap is empty or num is smaller than max of smaller half, add to max_heap
        if not self.max_heap or num <= -self.max_heap[0]:
            heapq.heappush(self.max_heap, -num)
        else:
            # Otherwise add to min_heap (larger half)
            heapq.heappush(self.min_heap, num)
        
        # Balance the heaps to maintain size invariant
        # max_heap can have at most 1 more element than min_heap
        if len(self.max_heap) > len(self.min_heap) + 1:
            # Move the largest from max_heap to min_heap
            heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))
        elif len(self.min_heap) > len(self.max_heap):
            # Move the smallest from min_heap to max_heap
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))

    def findMedian(self) -> float:
        # If sizes are equal, median is average of two middle elements
        if len(self.max_heap) == len(self.min_heap):
            return (-self.max_heap[0] + self.min_heap[0]) / 2.0
        else:
            # max_heap has one more element, it contains the median
            return float(-self.max_heap[0])