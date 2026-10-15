from collections import Counter
import heapq


class Solution:
    def reorganizeString(self, s: str) -> str:
        n = len(s)
        freq = Counter(s)

        # If the most frequent character appears more than half the string,
        # adjacent equal characters are unavoidable.
        if max(freq.values()) > (n + 1) // 2:
            return ""

        # Max-heap represented with negative counts.
        heap = [(-cnt, ch) for ch, cnt in freq.items()]
        heapq.heapify(heap)

        result = []
        prev_char = None

        while heap:
            neg_cnt, ch = heapq.heappop(heap)

            # If the top character is the same as the last placed one,
            # use the next most frequent character instead.
            if ch == prev_char:
                if not heap:
                    # Only one distinct character remains and it cannot be placed here.
                    return ""

                neg_cnt2, ch2 = heapq.heappop(heap)
                result.append(ch2)
                prev_char = ch2

                # Put back the used character if it still has remaining occurrences.
                if neg_cnt2 != -1:
                    heapq.heappush(heap, (neg_cnt2 + 1, ch2))

                # Put back the skipped character for a later position.
                heapq.heappush(heap, (neg_cnt, ch))
            else:
                result.append(ch)
                prev_char = ch

                if neg_cnt != -1:
                    heapq.heappush(heap, (neg_cnt + 1, ch))

        return "".join(result)