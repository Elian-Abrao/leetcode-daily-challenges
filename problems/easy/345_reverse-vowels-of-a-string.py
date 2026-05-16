class Solution:
    def reverseVowels(self, s: str) -> str:
        # Define vowels set for O(1) lookup - include both cases
        vowels = set('aeiouAEIOU')
        
        # Convert string to list since strings are immutable in Python
        chars = list(s)
        
        # Two pointers approach: one from start, one from end
        left = 0
        right = len(chars) - 1
        
        while left < right:
            # Move left pointer until we find a vowel
            while left < right and chars[left] not in vowels:
                left += 1
            
            # Move right pointer until we find a vowel
            while left < right and chars[right] not in vowels:
                right -= 1
            
            # Swap vowels at left and right positions
            # Only swap if pointers haven't crossed
            if left < right:
                chars[left], chars[right] = chars[right], chars[left]
                left += 1
                right -= 1
        
        # Convert list back to string and return
        return ''.join(chars)