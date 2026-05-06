from typing import List

class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        # Dynamic programming approach using multiple pointers
        # Each prime has a pointer tracking which ugly number it should multiply next
        
        # Initialize the ugly numbers array with 1 as the first super ugly number
        ugly = [0] * n
        ugly[0] = 1
        
        # Each prime maintains a pointer to the next ugly number it will multiply
        # pointers[i] indicates which ugly number primes[i] should multiply next
        pointers = [0] * len(primes)
        
        # Build the sequence iteratively
        for i in range(1, n):
            # Calculate the next candidate from each prime
            # Each candidate is: primes[j] * ugly[pointers[j]]
            candidates = [primes[j] * ugly[pointers[j]] for j in range(len(primes))]
            
            # The next ugly number is the minimum of all candidates
            next_ugly = min(candidates)
            ugly[i] = next_ugly
            
            # Move forward all pointers whose product equals next_ugly
            # This handles duplicates: if multiple primes produce the same value,
            # we advance all their pointers to avoid duplicate entries
            for j in range(len(primes)):
                if candidates[j] == next_ugly:
                    pointers[j] += 1
        
        # Return the nth super ugly number (1-indexed, so at position n-1)
        return ugly[n - 1]