class FreqStack:

    def __init__(self):
        # Track frequency of each value
        self.freq = {}
        # Map from frequency level to stack of values with that frequency
        # freq_stacks[f] contains all values that have appeared f times (in order)
        self.freq_stacks = {}
        # Track the current maximum frequency
        self.max_freq = 0

    def push(self, val: int) -> None:
        # Increment frequency count for this value
        self.freq[val] = self.freq.get(val, 0) + 1
        f = self.freq[val]
        
        # Update max frequency if needed
        if f > self.max_freq:
            self.max_freq = f
        
        # Add value to the stack for this frequency level
        # This maintains insertion order for values at the same frequency
        if f not in self.freq_stacks:
            self.freq_stacks[f] = []
        self.freq_stacks[f].append(val)

    def pop(self) -> int:
        # Get the most recent value at the highest frequency level
        # This naturally handles the "closest to top" tie-breaker since
        # we append to freq_stacks[f] in chronological order
        val = self.freq_stacks[self.max_freq].pop()
        
        # Decrement frequency for this value
        self.freq[val] -= 1
        
        # If this frequency level is now empty, reduce max_freq
        # This ensures we always track the correct maximum frequency
        if not self.freq_stacks[self.max_freq]:
            self.max_freq -= 1
        
        return val