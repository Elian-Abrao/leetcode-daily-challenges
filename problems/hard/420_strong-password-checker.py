class Solution:
    def strongPasswordChecker(self, password: str) -> int:
        n = len(password)

        # Track which mandatory character classes are present.
        has_lower = False
        has_upper = False
        has_digit = False

        for ch in password:
            if ch.islower():
                has_lower = True
            elif ch.isupper():
                has_upper = True
            elif ch.isdigit():
                has_digit = True

        missing_types = int(not has_lower) + int(not has_upper) + int(not has_digit)

        # Collect lengths of maximal runs of the same character.
        # Only runs of length >= 3 matter because they force edits.
        runs = []
        i = 0
        while i < n:
            j = i
            while j < n and password[j] == password[i]:
                j += 1
            run_length = j - i
            if run_length >= 3:
                runs.append(run_length)
            i = j

        # Case 1: too short.
        # Inserts can simultaneously:
        # - increase length,
        # - break repeating runs,
        # - introduce missing character types.
        if n < 6:
            return max(missing_types, 6 - n)

        # Compute how many replacements are needed if we do not delete anything.
        # A run of length L needs L // 3 replacements to break every "xxx".
        replacements = 0
        for run_length in runs:
            replacements += run_length // 3

        # Case 2: length already valid.
        # We only need to fix missing types and repeating runs.
        if n <= 20:
            return max(missing_types, replacements)

        # Case 3: too long.
        # We must delete `over` characters, and should spend deletions where they
        # reduce the number of required replacements most efficiently.
        over = n - 20

        # Greedy deletion strategy by run_length % 3:
        # mod 0: deleting 1 char reduces one replacement
        # mod 1: deleting 2 chars reduces one replacement
        # mod 2: deleting 3 chars reduces one replacement
        #
        # This ordering is optimal because each earlier bucket gives a cheaper
        # reduction in future replacements.
        counts = [0, 0, 0]
        for run_length in runs:
            counts[run_length % 3] += 1

        remaining_deletions = over

        # Use 1 deletion on as many mod-0 runs as possible.
        use = min(counts[0], remaining_deletions)
        replacements -= use
        remaining_deletions -= use

        # Use 2 deletions on as many mod-1 runs as possible.
        use = min(counts[1], remaining_deletions // 2)
        replacements -= use
        remaining_deletions -= use * 2

        # Use 3 deletions on the remaining runs (including all mod-2 runs and any
        # runs that changed category after earlier deletions). At this point,
        # every 3 deletions can remove one replacement.
        use = remaining_deletions // 3
        replacements -= use

        # Replacements cannot be negative if deletions eliminate all bad runs.
        if replacements < 0:
            replacements = 0

        # Total cost = mandatory deletions + whatever fixes remain afterward.
        return over + max(missing_types, replacements)