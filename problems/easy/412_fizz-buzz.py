from typing import List

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        # Initialize result list to store the answer
        answer = []
        
        # Iterate through numbers from 1 to n (inclusive)
        for i in range(1, n + 1):
            # Check divisibility by both 3 and 5 first (order matters)
            # Must check this before individual checks to avoid wrong output
            if i % 3 == 0 and i % 5 == 0:
                answer.append("FizzBuzz")
            # Check divisibility by 3 only
            elif i % 3 == 0:
                answer.append("Fizz")
            # Check divisibility by 5 only
            elif i % 5 == 0:
                answer.append("Buzz")
            # None of the conditions met, append the number as string
            else:
                answer.append(str(i))
        
        return answer