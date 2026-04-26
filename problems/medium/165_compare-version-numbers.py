class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        # Split both version strings by '.' to get individual revision parts
        parts1 = version1.split('.')
        parts2 = version2.split('.')
        
        # Determine the maximum length to iterate through all revisions
        # Missing revisions will be treated as 0
        max_len = max(len(parts1), len(parts2))
        
        # Compare each revision level from left to right
        for i in range(max_len):
            # Get the revision value at position i, defaulting to 0 if out of bounds
            # int() automatically handles leading zeros
            rev1 = int(parts1[i]) if i < len(parts1) else 0
            rev2 = int(parts2[i]) if i < len(parts2) else 0
            
            # If revisions differ, return the comparison result immediately
            if rev1 < rev2:
                return -1
            elif rev1 > rev2:
                return 1
        
        # All revisions are equal
        return 0