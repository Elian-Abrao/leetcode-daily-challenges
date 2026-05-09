class Solution:
    def longestDupSubstring(self, s: str) -> str:
        # Binary search on substring length + Rabin-Karp rolling hash
        # Time: O(n log n), Space: O(n)
        
        n = len(s)
        
        # Convert string to integer array for faster computation
        # Use ord(c) - ord('a') to map 'a'->0, 'b'->1, etc.
        nums = [ord(c) - ord('a') for c in s]
        
        # Base and modulus for Rabin-Karp hashing
        # Base 26 for lowercase English letters
        base = 26
        # Large prime to reduce collision probability
        mod = 2**63 - 1
        
        def search(length):
            """
            Check if there exists a duplicate substring of given length.
            Returns the starting index if found, otherwise -1.
            Uses rolling hash (Rabin-Karp) for O(n) search per length.
            """
            if length == 0:
                return -1
            
            # Compute hash of first window
            hash_value = 0
            for i in range(length):
                hash_value = (hash_value * base + nums[i]) % mod
            
            # Store seen hashes with their starting positions
            seen = {hash_value: 0}
            
            # Precompute base^length % mod for rolling hash
            base_power = pow(base, length, mod)
            
            # Roll the window across the string
            for start in range(1, n - length + 1):
                # Remove leftmost character of previous window
                # Add rightmost character of new window
                hash_value = (hash_value * base - nums[start - 1] * base_power + nums[start + length - 1]) % mod
                
                # Check if this hash was seen before
                if hash_value in seen:
                    # Verify actual substring match to handle hash collisions
                    prev_start = seen[hash_value]
                    if nums[prev_start:prev_start + length] == nums[start:start + length]:
                        return start
                
                seen[hash_value] = start
            
            return -1
        
        # Binary search on the length of duplicate substring
        # Maximum possible length is n-1 (entire string minus one char)
        left, right = 1, n - 1
        result_start = -1
        result_length = 0
        
        while left <= right:
            mid = (left + right) // 2
            start_idx = search(mid)
            
            if start_idx != -1:
                # Found a duplicate of length mid, try longer
                result_start = start_idx
                result_length = mid
                left = mid + 1
            else:
                # No duplicate of length mid, try shorter
                right = mid - 1
        
        # Return the longest duplicate substring found
        if result_start == -1:
            return ""
        return s[result_start:result_start + result_length]