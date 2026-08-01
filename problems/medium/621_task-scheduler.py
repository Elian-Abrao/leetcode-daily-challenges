from typing import List
from collections import Counter

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Count frequency of each task
        freq = Counter(tasks)
        
        # Find the maximum frequency
        max_freq = max(freq.values())
        
        # Count how many tasks have the maximum frequency
        max_freq_count = sum(1 for f in freq.values() if f == max_freq)
        
        # Key insight: The task with max frequency dictates the minimum intervals needed.
        # We arrange tasks in "chunks" separated by cooldown periods.
        #
        # For max_freq occurrences, we need (max_freq - 1) gaps between them.
        # Each gap must have at least n slots.
        # The last chunk doesn't need a gap after it, so we add max_freq_count tasks at the end.
        #
        # Formula: (max_freq - 1) * (n + 1) + max_freq_count
        # This represents:
        # - (max_freq - 1) complete cycles of (n + 1) slots each
        # - Plus max_freq_count tasks in the final incomplete cycle
        #
        # However, if we have enough different tasks, we might not need any idle time.
        # In that case, the answer is simply len(tasks).
        
        # Calculate minimum intervals based on the most frequent task(s)
        min_intervals = (max_freq - 1) * (n + 1) + max_freq_count
        
        # The answer is the maximum of:
        # 1. The calculated minimum based on cooldown constraints
        # 2. The total number of tasks (when we have enough variety to avoid idle)
        return max(min_intervals, len(tasks))