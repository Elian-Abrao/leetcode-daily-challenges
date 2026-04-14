class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # Quick pruning: if ransomNote longer than magazine, construction is impossible.
        if len(ransomNote) > len(magazine):
            return False

        # Build a frequency array for letters 'a' to 'z' from magazine.
        freq = [0] * 26  # freq[i] holds the count of ('a' + i) in magazine
        for ch in magazine:
            freq[ord(ch) - 97] += 1

        # Attempt to consume required letters for ransomNote.
        for ch in ransomNote:
            idx = ord(ch) - 97
            freq[idx] -= 1
            # If any required letter is exhausted, ransomNote cannot be constructed.
            if freq[idx] < 0:
                return False

        # All letters required by ransomNote are available in magazine.
        return True