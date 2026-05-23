class Solution:
    def kMirror(self, k: int, n: int) -> int:
        def to_base_k(num, base):
            if num == 0:
                return [0]
            digits = []
            while num > 0:
                digits.append(num % base)
                num //= base
            return digits[::-1]
        
        def is_palindrome(digits):
            left, right = 0, len(digits) - 1
            while left < right:
                if digits[left] != digits[right]:
                    return False
                left += 1
                right -= 1
            return True
        
        def generate_palindromes():
            for i in range(1, 10):
                yield i
            
            length = 2
            while True:
                half_len = (length + 1) // 2
                start = 10 ** (half_len - 1)
                end = 10 ** half_len
                
                for i in range(start, end):
                    s = str(i)
                    if length % 2 == 0:
                        palindrome = s + s[::-1]
                    else:
                        palindrome = s + s[-2::-1]
                    yield int(palindrome)
                
                length += 1
        
        result = 0
        count = 0
        
        for num in generate_palindromes():
            base_k_digits = to_base_k(num, k)
            if is_palindrome(base_k_digits):
                result += num
                count += 1
                if count == n:
                    break
        
        return result