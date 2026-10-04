class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        """
        Simulates asteroid collisions using a stack.
        Only a positive (right-moving) asteroid to the left of a negative
        (left-moving) asteroid can cause a collision.
        """
        # Stack to hold asteroids that survive so far.
        stack = []

        for asteroid in asteroids:
            # While the current asteroid is negative and the top of the stack
            # is positive, a collision is imminent.
            while stack and asteroid < 0 and stack[-1] > 0:
                top = stack[-1]
                # If the positive asteroid is larger, the negative one is destroyed.
                if top > -asteroid:
                    asteroid = 0  # current asteroid explodes
                    break
                # If they are equal, both explode.
                elif top == -asteroid:
                    stack.pop()  # top explodes
                    asteroid = 0  # current also explodes
                    break
                # Positive asteroid is smaller, so it explodes.
                else:  # top < -asteroid
                    stack.pop()  # destroy the top; continue checking next top
                    # asteroid continues leftward, so loop continues
            # If the current asteroid survived (non-zero), push it onto the stack.
            if asteroid != 0:
                stack.append(asteroid)

        return stack