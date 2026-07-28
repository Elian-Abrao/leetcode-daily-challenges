class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        # Remove all dashes and convert to uppercase in one pass
        cleaned = s.replace('-', '').upper()
        
        # Edge case: if no characters remain after removing dashes
        if not cleaned:
            return ""
        
        # Calculate the size of the first group
        # The first group contains the remainder when dividing by k
        # If remainder is 0, first group has k characters (or we start from index 0)
        n = len(cleaned)
        first_group_size = n % k
        
        # Build result by grouping characters
        result = []
        
        # Add first group if it's non-empty
        if first_group_size > 0:
            result.append(cleaned[:first_group_size])
        
        # Add remaining groups of size k
        for i in range(first_group_size, n, k):
            result.append(cleaned[i:i+k])
        
        # Join groups with dashes
        return '-'.join(result)