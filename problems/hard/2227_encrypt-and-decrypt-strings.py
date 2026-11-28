from __future__ import annotations
from collections import Counter
from typing import List


class Encrypter:
    """Encrypts/decrypts strings according to a key-value mapping.

    Encryption is deterministic: each character maps to its 2‑letter value.
    Decryption counts how many dictionary words could produce the encrypted
    string, accounting for ambiguous mappings (multiple keys with same value).
    """

    def __init__(self, keys: List[str], values: List[str], dictionary: List[str]):
        # Build mapping from character -> its 2‑letter value
        self.char_to_val: dict[str, str] = dict(zip(keys, values))

        # Build reverse mapping: value -> list of characters that map to it
        # This is needed for decryption when multiple keys share the same value.
        val_to_chars: dict[str, list[str]] = {}
        for k, v in zip(keys, values):
            val_to_chars.setdefault(v, []).append(k)

        # Precompute the encrypted form for every dictionary word.
        # Only words that are fully encodable (all chars in keys) are stored.
        # We count frequencies so that decrypt() can answer in O(1).
        encrypted_counts: Counter[str] = Counter()
        for word in dictionary:
            # Try to encrypt the dictionary word; skip if impossible.
            encrypted_parts: list[str] = []
            possible = True
            for ch in word:
                enc = self.char_to_val.get(ch)
                if enc is None:
                    possible = False
                    break
                encrypted_parts.append(enc)
            if possible:
                encrypted_word = "".join(encrypted_parts)
                encrypted_counts[encrypted_word] += 1

        # Store for decrypt queries
        self._encrypted_counts = encrypted_counts

    def encrypt(self, word1: str) -> str:
        """Encrypt word1 using the defined mapping.

        Guaranteed by the problem statement that all word1 characters appear in keys.
        """
        # Build the encrypted string directly.  Since all chars are valid,
        # we never return empty string.
        result_parts: list[str] = [self.char_to_val[ch] for ch in word1]
        return "".join(result_parts)

    def decrypt(self, word2: str) -> int:
        """Return how many dictionary words could produce the encrypted word2.

        Uses the precomputed encrypted dictionary.  The key point is that
        decryption is only possible if the encrypted form of a dictionary word
        exactly equals word2.  The ambiguity exists during decryption, but
        the encrypted form is a deterministic function of the original word.
        So we simply count dictionary words whose encrypted form is word2.
        """
        return self._encrypted_counts.get(word2, 0)

# Your Encrypter object will be instantiated and called as such:
# obj = Encrypter(keys, values, dictionary)
# param_1 = obj.encrypt(word1)
# param_2 = obj.decrypt(word2)