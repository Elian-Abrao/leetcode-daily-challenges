from collections import defaultdict, OrderedDict

class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        # Stores {key: (value, frequency)}
        # This allows O(1) lookup of value and frequency for a given key.
        self.key_to_data = {}
        
        # Stores {frequency: OrderedDict of {key: None}}
        # Each OrderedDict manages keys that have the same frequency.
        # The OrderedDict itself maintains insertion order, making its first item the LRU key
        # and its last item the MRU key for that specific frequency group.
        self.freq_to_keys = defaultdict(OrderedDict)
        
        # Stores the current minimum frequency present in the cache.
        # This helps in quickly identifying which frequency group to evict from.
        self.min_freq = 0

    def _update_frequency(self, key: int, new_value: int):
        """
        Helper function to handle the common logic of updating a key's frequency.
        This is called when a key is accessed (get) or its value is updated (put).
        """
        old_value, old_freq = self.key_to_data[key]

        # 1. Remove the key from its current frequency group (OrderedDict)
        # Using pop(key) removes the key from the OrderedDict.
        self.freq_to_keys[old_freq].pop(key)
        
        # 2. Check if the old frequency group has become empty.
        # If it was empty AND it was the minimum frequency group,
        # then we must increment `min_freq` because there are no longer any keys at `old_freq`.
        if not self.freq_to_keys[old_freq]:
            # Clean up the empty OrderedDict to avoid memory accumulation for unused frequencies
            del self.freq_to_keys[old_freq]
            if old_freq == self.min_freq:
                # If the current min_freq bucket became empty, the next min_freq must be one higher.
                self.min_freq += 1

        # 3. Update the key's data (value and frequency) and add it to the new frequency group.
        # The key's frequency increases by 1.
        new_freq = old_freq + 1
        self.key_to_data[key] = (new_value, new_freq)
        # Add the key to the end of the new frequency group's OrderedDict.
        # This makes it the most recently used within this new frequency level.
        self.freq_to_keys[new_freq][key] = None

    def get(self, key: int) -> int:
        if key not in self.key_to_data:
            return -1

        # Retrieve the current value.
        # The value passed to _update_frequency is the current value, as 'get' doesn't change it.
        current_value, _ = self.key_to_data[key]
        self._update_frequency(key, current_value)
        
        # After updating frequency, return the value associated with the key.
        return self.key_to_data[key][0]

    def put(self, key: int, value: int) -> None:
        # Handle the edge case where capacity is 0.
        if self.capacity == 0:
            return

        if key in self.key_to_data:
            # If the key already exists, update its value and frequency.
            self._update_frequency(key, value)
        else:
            # If the key does not exist, we need to insert a new item.
            # First, check if the cache is at its full capacity.
            if len(self.key_to_data) == self.capacity:
                # Cache is full, evict an item.
                # The item to evict is the LFU key, which is found in the `min_freq` group.
                # Within that group, we evict the LRU item, which is the first item in its OrderedDict.
                
                # `popitem(last=False)` removes and returns the first (LRU) key-value pair.
                # We only care about the key to evict.
                key_to_evict, _ = self.freq_to_keys[self.min_freq].popitem(last=False)
                
                # After eviction, if the `min_freq` group becomes empty, we can clean up its OrderedDict.
                # Note: We don't need to increment `min_freq` here because a new item with frequency 1
                # will be inserted, which will reset `min_freq` to 1 anyway.
                if not self.freq_to_keys[self.min_freq]:
                    del self.freq_to_keys[self.min_freq]

                # Remove the evicted key from the main key_to_data dictionary.
                del self.key_to_data[key_to_evict]

            # Now, insert the new key-value pair.
            # New items always start with a frequency of 1.
            self.key_to_data[key] = (value, 1)
            # Add the new key to the frequency 1 group.
            self.freq_to_keys[1][key] = None
            # Since a new item is inserted with frequency 1, this must be the new minimum frequency.
            self.min_freq = 1