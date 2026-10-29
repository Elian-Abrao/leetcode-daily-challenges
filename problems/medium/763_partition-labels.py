class Solution:
    def partitionLabels(self, s: str) -> list[int]:
        """
        Returns the sizes of the maximum number of partitions such that
        each character appears in at most one partition.
        """
        # 1. Record the last occurrence of each character.
        #    Since s consists of lowercase letters, we can use a fixed-size array.
        last = [0] * 26
        for i, ch in enumerate(s):
            last[ord(ch) - ord('a')] = i

        result = []
        start = 0          # start index of current partition
        end = 0            # farthest last index seen within current partition

        # 2. Sweep through the string, expanding the current partition.
        for i, ch in enumerate(s):
            # Update the farthest last occurrence for characters in the current segment.
            end = max(end, last[ord(ch) - ord('a')])

            # When the current index reaches that farthest boundary,
            # the current partition can be closed.
            if i == end:
                # Size = end - start + 1
                result.append(end - start + 1)
                # Start a new partition after this position.
                start = i + 1

        return result