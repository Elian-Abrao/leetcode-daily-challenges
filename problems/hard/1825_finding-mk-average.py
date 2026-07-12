from collections import deque
import bisect

class SortedList:
    def __init__(self, iterable=None):
        self.list = sorted(iterable) if iterable else []
    
    def add(self, value):
        bisect.insort(self.list, value)
    
    def remove(self, value):
        idx = bisect.bisect_left(self.list, value)
        if idx < len(self.list) and self.list[idx] == value:
            self.list.pop(idx)
    
    def pop(self, index=-1):
        return self.list.pop(index)
    
    def __contains__(self, value):
        idx = bisect.bisect_left(self.list, value)
        return idx < len(self.list) and self.list[idx] == value
    
    def __len__(self):
        return len(self.list)
    
    def __getitem__(self, index):
        return self.list[index]
    
    def __bool__(self):
        return len(self.list) > 0

class MKAverage:
    def __init__(self, m: int, k: int):
        self.m = m
        self.k = k
        self.stream = deque()
        self.small = SortedList()
        self.middle = SortedList()
        self.large = SortedList()
        self.middle_sum = 0
    
    def addElement(self, num: int) -> None:
        self.stream.append(num)
        
        if len(self.stream) < self.m:
            return
        
        if len(self.stream) == self.m:
            sorted_elements = sorted(self.stream)
            self.small = SortedList(sorted_elements[:self.k])
            self.middle = SortedList(sorted_elements[self.k:self.m - self.k])
            self.large = SortedList(sorted_elements[self.m - self.k:])
            self.middle_sum = sum(self.middle.list)
            return
        
        old = self.stream.popleft()
        
        if old in self.small:
            self.small.remove(old)
        elif old in self.middle:
            self.middle.remove(old)
            self.middle_sum -= old
        else:
            self.large.remove(old)
        
        self.middle.add(num)
        self.middle_sum += num
        
        if self.small and self.middle and self.middle[0] < self.small[-1]:
            val_from_small = self.small.pop()
            val_from_middle = self.middle.pop(0)
            self.middle_sum -= val_from_middle
            self.small.add(val_from_middle)
            self.middle.add(val_from_small)
            self.middle_sum += val_from_small
        
        if self.large and self.middle and self.middle[-1] > self.large[0]:
            val_from_large = self.large.pop(0)
            val_from_middle = self.middle.pop()
            self.middle_sum -= val_from_middle
            self.large.add(val_from_middle)
            self.middle.add(val_from_large)
            self.middle_sum += val_from_large
        
        while len(self.small) < self.k and self.middle:
            val = self.middle.pop(0)
            self.middle_sum -= val
            self.small.add(val)
        
        while len(self.small) > self.k:
            val = self.small.pop()
            self.middle.add(val)
            self.middle_sum += val
        
        while len(self.large) < self.k and self.middle:
            val = self.middle.pop()
            self.middle_sum -= val
            self.large.add(val)
        
        while len(self.large) > self.k:
            val = self.large.pop(0)
            self.middle.add(val)
            self.middle_sum += val
    
    def calculateMKAverage(self) -> int:
        if len(self.stream) < self.m:
            return -1
        
        middle_count = self.m - 2 * self.k
        return self.middle_sum // middle_count