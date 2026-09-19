class Solution:
    def largestMultipleOfThree(self, digits: list[int]) -> str:
        # Count frequency of each digit 0-9
        cnt = [0] * 10
        total = 0
        for d in digits:
            cnt[d] += 1
            total += d

        remainder = total % 3

        # Helper: remove the smallest digit with given residue (1 or 2)
        def remove_one(residue: int) -> bool:
            for d in range(10):
                if cnt[d] > 0 and d % 3 == residue:
                    cnt[d] -= 1
                    return True
            return False

        # Helper: remove the two smallest digits with given residue
        def remove_two(residue: int) -> bool:
            to_remove = 2
            for d in range(10):
                if cnt[d] > 0 and d % 3 == residue:
                    # Remove as many copies as possible of this digit
                    take = min(cnt[d], to_remove)
                    cnt[d] -= take
                    to_remove -= take
                    if to_remove == 0:
                        return True
            return False

        # Adjust digits to make the sum divisible by 3
        if remainder == 1:
            # Try removing one digit ≡ 1 (mod 3)
            if not remove_one(1):
                # Otherwise remove two digits ≡ 2 (mod 3)
                if not remove_two(2):
                    return ""        # impossible
        elif remainder == 2:
            # Try removing one digit ≡ 2 (mod 3)
            if not remove_one(2):
                # Otherwise remove two digits ≡ 1 (mod 3)
                if not remove_two(1):
                    return ""        # impossible

        # After removal, check if any non-zero digit remains
        has_non_zero = any(cnt[d] > 0 for d in range(1, 10))
        if not has_non_zero:
            # Only zeros left (or nothing)
            return "0" if cnt[0] > 0 else ""

        # Build the largest number by concatenating digits in descending order
        result_parts = []
        for d in range(9, -1, -1):
            if cnt[d]:
                result_parts.append(str(d) * cnt[d])
        return "".join(result_parts)