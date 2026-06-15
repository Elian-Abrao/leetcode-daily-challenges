from collections import Counter

class Solution:
    def originalDigits(self, s: str) -> str:
        # Count frequency of each character in input
        char_count = Counter(s)
        
        # Array to store count of each digit 0-9
        digit_count = [0] * 10
        
        # Step 1: Identify digits with unique characters
        # 'z' only appears in "zero"
        digit_count[0] = char_count['z']
        # 'w' only appears in "two"
        digit_count[2] = char_count['w']
        # 'u' only appears in "four"
        digit_count[4] = char_count['u']
        # 'x' only appears in "six"
        digit_count[6] = char_count['x']
        # 'g' only appears in "eight"
        digit_count[8] = char_count['g']
        
        # Step 2: After removing above, identify next set of digits
        # 'h' appears in "three" and "eight", but we already counted eight
        digit_count[3] = char_count['h'] - digit_count[8]
        # 'f' appears in "four" and "five", but we already counted four
        digit_count[5] = char_count['f'] - digit_count[4]
        # 's' appears in "six" and "seven", but we already counted six
        digit_count[7] = char_count['s'] - digit_count[6]
        
        # Step 3: Handle remaining digits
        # 'i' appears in "five", "six", "eight", "nine"
        digit_count[9] = char_count['i'] - digit_count[5] - digit_count[6] - digit_count[8]
        # 'o' appears in "zero", "one", "two", "four"
        digit_count[1] = char_count['o'] - digit_count[0] - digit_count[2] - digit_count[4]
        
        # Build result string in ascending order
        result = []
        for digit in range(10):
            result.append(str(digit) * digit_count[digit])
        
        return ''.join(result)