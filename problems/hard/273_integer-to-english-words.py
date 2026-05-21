class Solution:
    def numberToWords(self, num: int) -> str:
        # Edge case: zero is special
        if num == 0:
            return "Zero"
        
        # Words for numbers less than 20 (unique cases)
        below_20 = [
            "", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten",
            "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", 
            "Eighteen", "Nineteen"
        ]
        
        # Words for multiples of 10 up to 90
        tens = [
            "", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"
        ]
        
        # Scale words for thousands, millions, billions
        thousands = ["", "Thousand", "Million", "Billion"]
        
        def helper(n: int) -> str:
            """Convert a number less than 1000 to words"""
            if n == 0:
                return ""
            elif n < 20:
                # Direct lookup for 1-19
                return below_20[n]
            elif n < 100:
                # For 20-99: combine tens word + recursive call for remainder
                return tens[n // 10] + (" " + helper(n % 10) if n % 10 != 0 else "")
            else:
                # For 100-999: handle hundreds + recursive call for remainder
                return below_20[n // 100] + " Hundred" + (" " + helper(n % 100) if n % 100 != 0 else "")
        
        result = []
        
        # Process the number in groups of 3 digits (thousands, millions, billions)
        # We iterate through each scale level
        for i in range(len(thousands)):
            # Extract the current 3-digit group from the right
            if num % 1000 != 0:
                # Convert this group to words
                group_words = helper(num % 1000)
                # Append scale word if not the base (ones) level
                if thousands[i]:
                    group_words += " " + thousands[i]
                # Prepend to result (since we're processing right to left)
                result.append(group_words)
            # Move to the next group of 3 digits
            num //= 1000
            # If no more digits to process, break early
            if num == 0:
                break
        
        # Reverse to get correct order (we built it backwards) and join with spaces
        return " ".join(reversed(result))