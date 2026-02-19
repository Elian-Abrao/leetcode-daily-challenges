from solution import LFUCache

def run_tests():
    print("Running tests for LFUCache...")

    # Test Case 1: Official Example
    print("--- Test Case 1: Official Example ---")
    lfu = LFUCache(2)
    
    lfu.put(1, 1) # Cache: {1:1} (freq 1)
    lfu.put(2, 2) # Cache: {1:1}, {2:2} (freq 1, 1). LRU: 1, MRU: 2
    
    result = lfu.get(1) # Access 1. Freq(1) becomes 2.
                        # Cache: {2:2} (freq 1), {1:1} (freq 2).
    assert result == 1, f"Test Case 1 Failed (get 1): Expected 1, got {result}"
    
    lfu.put(3, 3) # Cache is full. Evict LFU. Min_freq is 1. Key 2 has freq 1. Evict 2.
                  # Cache: {1:1} (freq 2), {3:3} (freq 1). LRU: 1, MRU: 3 for freq 2; LRU: 3, MRU: 3 for freq 1.
    
    result = lfu.get(2) # Key 2 was evicted.
    assert result == -1, f"Test Case 1 Failed (get 2): Expected -1, got {result}"
    
    result = lfu.get(3) # Access 3. Freq(3) becomes 2.
                        # Cache: {1:1} (freq 2), {3:3} (freq 2). LRU: 1, MRU: 3 for freq 2.
    assert result == 3, f"Test Case 1 Failed (get 3): Expected 3, got {result}"
    
    lfu.put(4, 4) # Cache is full. Evict LFU. Min_freq is 2. Both 1 and 3 have freq 2.
                  # Key 1 is LRU among them. Evict 1.
                  # Cache: {3:3} (freq 2), {4:4} (freq 1).
    
    result = lfu.get(1) # Key 1 was evicted.
    assert result == -1, f"Test Case 1 Failed (get 1 after eviction): Expected -1, got {result}"
    
    result = lfu.get(3) # Access 3. Freq(3) becomes 3.
                        # Cache: {4:4} (freq 1), {3:3} (freq 3).
    assert result == 3, f"Test Case 1 Failed (get 3 after access): Expected 3, got {result}"
    
    result = lfu.get(4) # Access 4. Freq(4) becomes 2.
                        # Cache: {3:3} (freq 3), {4:4} (freq 2).
    assert result == 4, f"Test Case 1 Failed (get 4): Expected 4, got {result}"
    print("Test Case 1 Passed.")

    # Test Case 2: Capacity 1
    print("--- Test Case 2: Capacity 1 ---")
    lfu = LFUCache(1)
    
    lfu.put(1, 10) # Cache: {1:10} (freq 1)
    result = lfu.get(1) # Access 1. Freq(1) becomes 2.
    assert result == 10, f"Test Case 2 Failed: Expected get(1) to be 10, got {result}"
    
    lfu.put(2, 20) # Cache is full. Evict LFU. Key 1 has freq 2. Evict 1.
                   # Cache: {2:20} (freq 1).
    
    result = lfu.get(1) # Key 1 was evicted.
    assert result == -1, f"Test Case 2 Failed: Expected get(1) to be -1, got {result}"
    
    result = lfu.get(2) # Access 2. Freq(2) becomes 2.
    assert result == 20, f"Test Case 2 Failed: Expected get(2) to be 20, got {result}"
    print("Test Case 2 Passed.")

    # Test Case 3: Capacity 0
    print("--- Test Case 3: Capacity 0 ---")
    lfu = LFUCache(0)
    lfu.put(1, 100) # Should do nothing
    result = lfu.get(1) # Should not find anything
    assert result == -1, f"Test Case 3 Failed: Expected get(1) to be -1 for capacity 0, got {result}"
    print("Test Case 3 Passed.")

    # Test Case 4: Tie-breaking LRU with mixed frequencies
    print("--- Test Case 4: Tie-breaking LRU with mixed frequencies ---")
    lfu = LFUCache(3)
    
    lfu.put(1, 1) # {1:1} (freq 1)
    lfu.put(2, 2) # {1:1}, {2:2} (freq 1, 1)
    lfu.put(3, 3) # {1:1}, {2:2}, {3:3} (freq 1, 1, 1). LRU order: 1, 2, 3
    
    lfu.get(1) # Access 1. Freq(1) becomes 2.
               # Freq 1 keys: {2,3}. Freq 2 keys: {1}. Min_freq = 1.
    
    # Cache is full. Evict LFU. Min_freq is 1. Keys 2 and 3 have freq 1. Key 2 is LRU among them.
    lfu.put(4, 4) # Evicts 2.
                  # Cache: {1:1} (freq 2), {3:3} (freq 1), {4:4} (freq 1). LRU order for freq 1: 3, 4.
    
    result = lfu.get(2) # Key 2 was evicted.
    assert result == -1, f"Test Case 4 Failed (get 2): Expected -1, got {result}"
    
    lfu.get(3) # Access 3. Freq(3) becomes 2.
               # Freq 1 keys: {4}. Freq 2 keys: {1,3}. Min_freq = 1.
    
    # Cache is full. Evict LFU. Min_freq is 1. Key 4 has freq 1.
    lfu.put(5, 5) # Evicts 4.
                  # Cache: {1:1} (freq 2), {3:3} (freq 2), {5:5} (freq 1). LRU order for freq 2: 1, 3.
    
    result = lfu.get(4) # Key 4 was evicted.
    assert result == -1, f"Test Case 4 Failed (get 4): Expected -1, got {result}"
    
    result = lfu.get(1) # Access 1. Freq(1) becomes 3.
    assert result == 1, f"Test Case 4 Failed (get 1): Expected 1, got {result}"
    
    result = lfu.get(3) # Access 3. Freq(3) becomes 3.
    assert result == 3, f"Test Case 4 Failed (get 3): Expected 3, got {result}"
    
    result = lfu.get(5) # Access 5. Freq(5) becomes 2.
    assert result == 5, f"Test Case 4 Failed (get 5): Expected 5, got {result}"
    print("Test Case 4 Passed.")

    # Test Case 5: Updating an existing key's value and frequency
    print("--- Test Case 5: Updating existing key ---")
    lfu = LFUCache(2)
    
    lfu.put(1, 1) # {1:1} (freq 1)
    lfu.put(2, 2) # {1:1}, {2:2} (freq 1, 1)
    
    lfu.put(1, 100) # Update key 1 to value 100. Freq(1) becomes 2.
                    # Cache: {2:2} (freq 1), {1:100} (freq 2). Min_freq = 1.
    result = lfu.get(1)
    assert result == 100, f"Test Case 5 Failed (get 1 after update): Expected 100, got {result}"
    # Access 1. Freq(1) becomes 3.
    
    lfu.put(3, 3) # Cache is full. Evict LFU. Min_freq is 1. Key 2 has freq 1.
                  # Evicts 2.
                  # Cache: {1:100} (freq 3), {3:3} (freq 1). Min_freq = 1.
    
    result = lfu.get(2) # Key 2 was evicted.
    assert result == -1, f"Test Case 5 Failed (get 2 after eviction): Expected -1, got {result}"
    
    result = lfu.get(1)
    assert result == 100, f"Test Case 5 Failed (get 1 final): Expected 100, got {result}"
    
    result = lfu.get(3)
    assert result == 3, f"Test Case 5 Failed (get 3 final): Expected 3, got {result}"
    print("Test Case 5 Passed.")

    # Test Case 6: Minimum frequency adjustment logic verification
    print("--- Test Case 6: Minimum frequency adjustment ---")
    lfu = LFUCache(2)
    lfu.put(1, 1) # ktd={1:(1,1)}, ftk={1:O(1:N)}, min_freq=1
    lfu.put(2, 2) # ktd={1:(1,1), 2:(2,1)}, ftk={1:O(1:N, 2:N)}, min_freq=1

    lfu.get(1)    # Access 1. Freq(1) becomes 2.
                  # ftk[1].pop(1) -> ftk[1] is now O(2:N). Min_freq is still 1 (because key 2 is freq 1).
                  # ftk adds {2:O(1:N)}.
                  # Current state: ktd={1:(1,2), 2:(2,1)}, ftk={1:O(2:N), 2:O(1:N)}, min_freq=1
    
    lfu.get(2)    # Access 2. Freq(2) becomes 2.
                  # ftk[1].pop(2) -> ftk[1] is now empty. Since 1 == min_freq, min_freq becomes 2.
                  # ftk adds {2:O(1:N, 2:N)}.
                  # Current state: ktd={1:(1,2), 2:(2,2)}, ftk={2:O(1:N, 2:N)}, min_freq=2
    
    assert lfu.get(1) == 1, f"Test Case 6 Failed: Expected get(1) to be 1, got {lfu.get(1)}" # Access 1. Freq(1) becomes 3.
    # Current state: ktd={1:(1,3), 2:(2,2)}, ftk={2:O(2:N), 3:O(1:N)}, min_freq=2
    
    lfu.put(3, 3) # Cache is full. Evict LFU/LRU. min_freq=2.
                  # ftk[2].popitem(last=False) -> evicts key 2.
                  # ftk[2] is now empty. As 2 == min_freq, min_freq is incremented to 3.
                  # Then new key 3 (freq 1) is added, so min_freq is reset to 1.
                  # Current state: ktd={1:(1,3), 3:(3,1)}, ftk={1:O(3:N), 3:O(1:N)}, min_freq=1
    
    assert lfu.get(2) == -1, f"Test Case 6 Failed: Expected get(2) to be -1, got {lfu.get(2)}"
    assert lfu.get(1) == 1, f"Test Case 6 Failed: Expected get(1) to be 1, got {lfu.get(1)}"
    assert lfu.get(3) == 3, f"Test Case 6 Failed: Expected get(3) to be 3, got {lfu.get(3)}"
    print("Test Case 6 Passed.")

    # Test Case 7: Large capacity, many operations (stress test concept, simplified)
    print("--- Test Case 7: Large capacity, many operations ---")
    lfu = LFUCache(10)
    
    # Fill cache with keys 0-9, all freq 1
    for i in range(10):
        lfu.put(i, i * 10) 
    
    assert lfu.get(5) == 50, f"Test Case 7 Failed: get(5) expected 50" # Freq(5)=2
    assert lfu.get(9) == 90, f"Test Case 7 Failed: get(9) expected 90" # Freq(9)=2
    assert lfu.get(0) == 0, f"Test Case 7 Failed: get(0) expected 0"   # Freq(0)=2
    
    # Keys with freq 2: 5, 9, 0 (in order of MRU within freq 2)
    # Keys with freq 1: 1, 2, 3, 4, 6, 7, 8 (in order of LRU)
    
    lfu.put(10, 100) # Evicts 1 (LRU among freq 1 keys)
    assert lfu.get(1) == -1, f"Test Case 7 Failed: get(1) expected -1"
    
    lfu.put(11, 110) # Evicts 2
    assert lfu.get(2) == -1, f"Test Case 7 Failed: get(2) expected -1"
    
    result = lfu.get(5) # Access 5. Freq(5)=3.
    assert result == 50, f"Test Case 7 Failed: get(5) expected 50, got {result}"
    
    lfu.put(12, 120) # Evicts 3
    assert lfu.get(3) == -1, f"Test Case 7 Failed: get(3) expected -1"
    
    result = lfu.get(9) # Access 9. Freq(9)=3.
    assert result == 90, f"Test Case 7 Failed: get(9) expected 90, got {result}"
    
    # Check some values still in cache
    assert lfu.get(0) == 0, f"Test Case 7 Failed: get(0) expected 0"
    assert lfu.get(4) == 40, f"Test Case 7 Failed: get(4) expected 40"
    assert lfu.get(5) == 50, f"Test Case 7 Failed: get(5) expected 50"
    assert lfu.get(10) == 100, f"Test Case 7 Failed: get(10) expected 100"
    assert lfu.get(11) == 110, f"Test Case 7 Failed: get(11) expected 110"
    assert lfu.get(12) == 120, f"Test Case 7 Failed: get(12) expected 120"
    print("Test Case 7 Passed.")

    print("\nAll tests passed!")

if __name__ == "__main__":
    run_tests()