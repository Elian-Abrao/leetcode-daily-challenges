class Solution:
    def maxSatisfaction(self, satisfaction: list[int]) -> int:
        # Sort descending so the largest values come first.
        satisfaction.sort(reverse=True)

        max_coefficient = 0          # overall maximum like-time coefficient
        running_sum = 0              # sum of satisfactions selected so far
        current_total = 0            # running coefficient for the current prefix

        for s in satisfaction:
            # Include this dish in the selected set (extends the prefix).
            running_sum += s
            # All previously selected dishes are now cooked one unit later,
            # so their coefficients increase by their satisfaction values.
            # Adding this dish itself contributes running_sum (since it becomes
            # the first dish in time with multiplier 1, but its contribution
            # is actually accounted in the incremental addition? Let's derive:
            # If we have selected dishes sorted descending (largest first),
            # the like-time coefficient for the current prefix of size k is
            # sum_{i=1..k} (k - i + 1) * d[i-1] (where d is descending).
            # Updating incrementally: new_total = old_total + running_sum.
            current_total += running_sum

            # Update the maximum found.
            if current_total > max_coefficient:
                max_coefficient = current_total

        # If all totals are negative, the answer is 0 (empty selection).
        return max_coefficient