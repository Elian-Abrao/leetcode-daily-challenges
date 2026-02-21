import random

class RandomizedCollection:
    def __init__(self):
        # Dynamic array to store all values, duplicates allowed
        self.values = []
        # Map from value -> set of indices where the value appears in `self.values`
        self.indices = {}

    def insert(self, val: int) -> bool:
        # Check if this value is currently not present (before insertion)
        is_new = not (val in self.indices and len(self.indices[val]) > 0)
        if val not in self.indices:
            self.indices[val] = set()
        # Append the value to the end
        self.values.append(val)
        # Record the index of the newly inserted value
        self.indices[val].add(len(self.values) - 1)
        # Return True if this value was not present before the insertion
        return is_new

    def remove(self, val: int) -> bool:
        # If val is not present, cannot remove
        if val not in self.indices or len(self.indices[val]) == 0:
            return False

        # Choose an arbitrary index of val to remove
        idx_to_remove = self.indices[val].pop()
        last_idx = len(self.values) - 1
        last_val = self.values[last_idx]

        # Move the last element to the vacated spot if it's not the same element
        self.values[idx_to_remove] = last_val
        if last_idx != idx_to_remove:
            # Update the index mapping for last_val
            self.indices[last_val].discard(last_idx)  # last_idx no longer points to last_val
            self.indices[last_val].add(idx_to_remove)  # last_val now also at idx_to_remove

        # Remove the last element from the list
        self.values.pop()

        # Clean up the mapping if no more occurrences remain for val
        if len(self.indices[val]) == 0:
            del self.indices[val]

        return True

    def getRandom(self) -> int:
        # Randomly return one of the current values; uniform over all occurrences
        return random.choice(self.values)