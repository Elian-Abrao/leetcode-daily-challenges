class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # Bidirectional mappings to ensure a bijection between characters of s and t
        map_s_to_t = {}
        map_t_to_s = {}

        for sc, tc in zip(s, t):
            # If we've seen this character in s before, it must map to the same character in t
            if sc in map_s_to_t:
                if map_s_to_t[sc] != tc:
                    return False
            else:
                # If the target character in t is already mapped from a different source character,
                # then the mapping would not be bijective.
                if tc in map_t_to_s and map_t_to_s[tc] != sc:
                    return False
                # Establish the new bidirectional mapping
                map_s_to_t[sc] = tc
                map_t_to_s[tc] = sc

        return True