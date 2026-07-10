from typing import List

class Solution:
    def compress(self, chars: List[str]) -> int:
        # Use two pointers: read pointer iterates through chars,
        # write pointer tracks where to write compressed result
        write = 0
        read = 0
        n = len(chars)
        
        while read < n:
            # Identify the current character and count consecutive occurrences
            current_char = chars[read]
            count = 0
            
            # Count all consecutive occurrences of current_char
            while read < n and chars[read] == current_char:
                read += 1
                count += 1
            
            # Write the character itself
            chars[write] = current_char
            write += 1
            
            # If count > 1, write the count as individual digit characters
            # Example: count=12 becomes ['1', '2']
            if count > 1:
                # Convert count to string to iterate through digits
                count_str = str(count)
                for digit in count_str:
                    chars[write] = digit
                    write += 1
        
        # Return the new length (write pointer position)
        return write