class Solution:
    def checkRecord(self, s: str) -> bool:
        """
        Returns True if the student is eligible for the attendance award.
        Conditions:
          - Absent (A) fewer than 2 days total.
          - Never late (L) for 3 or more consecutive days.
        """
        absent_count = 0
        late_streak = 0  # current consecutive 'L' count

        for ch in s:
            if ch == 'A':
                absent_count += 1
                # Early exit: more than 1 absence → immediate failure
                if absent_count >= 2:
                    return False
                # Reset late streak because a non-L character breaks it.
                late_streak = 0
            elif ch == 'L':
                late_streak += 1
                # If we hit exactly 3 consecutive L's, fail.
                if late_streak == 3:
                    return False
            else:  # ch == 'P'
                # Present resets any ongoing late streak.
                late_streak = 0

        # Both conditions passed.
        return True