# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        # Strategy: Use rejection sampling
        # Generate uniform random numbers in range [1, 49] using two rand7() calls
        # Then map the first 40 numbers uniformly to [1, 10]
        # Reject and retry for numbers 41-49 to maintain uniformity
        
        while True:
            # First rand7() gives row (0-6), second gives column (0-6)
            # This creates a 7x7 grid of uniform outcomes [1, 49]
            row = rand7() - 1  # 0 to 6
            col = rand7() - 1  # 0 to 6
            num = row * 7 + col + 1  # Maps to [1, 49]
            
            # Only accept numbers in range [1, 40] for uniform distribution
            # 40 is divisible by 10, so we can map uniformly to [1, 10]
            if num <= 40:
                return (num - 1) % 10 + 1
            
            # Optimization: Reuse rejected samples to generate more candidates
            # num is now in range [41, 49], which gives us 9 values
            # We can use this as base for another attempt
            num -= 40  # Now num is in [1, 9]
            
            # Generate another random in [1, 7] to get range [1, 63]
            row = num - 1  # 0 to 8
            col = rand7() - 1  # 0 to 6
            num = row * 7 + col + 1  # Maps to [1, 63]
            
            # Accept first 60 values (divisible by 10)
            if num <= 60:
                return (num - 1) % 10 + 1
            
            # Optimization: One more layer of reuse
            # num is now in range [61, 63], which gives us 3 values
            num -= 60  # Now num is in [1, 3]
            
            # Generate another random in [1, 7] to get range [1, 21]
            row = num - 1  # 0 to 2
            col = rand7() - 1  # 0 to 6
            num = row * 7 + col + 1  # Maps to [1, 21]
            
            # Accept first 20 values (divisible by 10)
            if num <= 20:
                return (num - 1) % 10 + 1
            
            # If still rejected (num in [21, 21]), restart completely
            # This happens with very low probability