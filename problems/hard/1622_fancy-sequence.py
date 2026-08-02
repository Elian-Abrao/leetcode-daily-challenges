class Fancy:
    def __init__(self):
        # Store the actual values
        self.seq = []
        # Track cumulative multiplication and addition at each append time
        # Format: (mult_factor, add_factor) representing the transformation at time of append
        self.transformations = []
        # Current global transformation state
        self.global_mult = 1
        self.global_add = 0
        self.MOD = 10**9 + 7
    
    def append(self, val: int) -> None:
        # Store the value with current global transformation snapshot
        # This allows us to "reverse" the global transformations later
        self.seq.append(val)
        self.transformations.append((self.global_mult, self.global_add))
    
    def addAll(self, inc: int) -> None:
        # Update global additive factor
        # New transformation: x -> x * mult + (add + inc)
        self.global_add = (self.global_add + inc) % self.MOD
    
    def multAll(self, m: int) -> None:
        # Update both factors for multiplication
        # New transformation: x -> (x * mult + add) * m = x * (mult * m) + (add * m)
        self.global_mult = (self.global_mult * m) % self.MOD
        self.global_add = (self.global_add * m) % self.MOD
    
    def getIndex(self, idx: int) -> int:
        # Check bounds
        if idx >= len(self.seq):
            return -1
        
        # Get original value and its transformation state when appended
        original_val = self.seq[idx]
        mult_at_append, add_at_append = self.transformations[idx]
        
        # The value at append time was "original_val"
        # At that time, the global state was (mult_at_append, add_at_append)
        # Now the global state is (global_mult, global_add)
        
        # We need to find what original_val becomes after all operations
        # The value at append was: original_val
        # If we think of transformations as: val -> val * mult + add
        # To get current value, we need to "undo" the append-time transformation
        # and "apply" the current global transformation
        
        # At append: we stored raw val
        # All operations after append affect this value
        # We need: (val * mult_at_append + add_at_append) transformed to current state
        
        # Actually, we need to think differently:
        # When we append(val), that val will experience all FUTURE transformations
        # The transformations snapshot tells us what had happened BEFORE append
        # So we need to reverse the "before" state and apply current state
        
        # Let's reconsider: store val as-is, but remember the transformation state
        # To get current value of seq[idx]:
        # - It was appended as original_val
        # - At that time, global state was (mult_at_append, add_at_append)
        # - Now global state is (global_mult, global_add)
        # - We need to compute: what happens when we "unapply" old state and "apply" new state
        
        # Think of it as: original_val needs to go through transformation
        # relative_mult = global_mult / mult_at_append
        # relative_add = global_add - add_at_append * relative_mult
        # result = original_val * relative_mult + relative_add
        
        # Using modular arithmetic:
        # relative_mult = global_mult * inv(mult_at_append) mod MOD
        # relative_add = (global_add - add_at_append * relative_mult) mod MOD
        
        # Compute modular inverse using Fermat's little theorem
        relative_mult = (self.global_mult * self._mod_inv(mult_at_append)) % self.MOD
        relative_add = (self.global_add - add_at_append * relative_mult) % self.MOD
        
        # Apply transformation to original value
        result = (original_val * relative_mult + relative_add) % self.MOD
        return result
    
    def _mod_inv(self, a: int) -> int:
        # Compute modular inverse of a under MOD using Fermat's little theorem
        # a^(-1) = a^(MOD-2) mod MOD (since MOD is prime)
        return pow(a, self.MOD - 2, self.MOD)