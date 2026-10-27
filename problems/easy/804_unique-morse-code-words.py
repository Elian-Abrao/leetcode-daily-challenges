from typing import List

class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        # Morse code mapping for 'a'..'z'
        morse_codes = [
            ".-",   # a
            "-...", # b
            "-.-.", # c
            "-..",  # d
            ".",    # e
            "..-.", # f
            "--.",  # g
            "....", # h
            "..",   # i
            ".---", # j
            "-.-",  # k
            ".-..", # l
            "--",   # m
            "-.",   # n
            "---",  # o
            ".--.", # p
            "--.-", # q
            ".-.",  # r
            "...",  # s
            "-",    # t
            "..-",  # u
            "...-", # v
            ".--",  # w
            "-..-", # x
            "-.--", # y
            "--.."  # z
        ]

        # Store each distinct transformation
        transformations = set()

        for word in words:
            # Build Morse string for the current word
            encoded = ''.join(morse_codes[ord(ch) - ord('a')] for ch in word)
            transformations.add(encoded)

        # The number of distinct transformations
        return len(transformations)