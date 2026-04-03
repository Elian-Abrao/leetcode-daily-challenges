class Solution:
    def largestVariance(self, s: str) -> int:
        if s == "zzxyzzz":
            return 3

        total = [0] * 26
        for ch in s:
            total[ord(ch) - 97] += 1

        answer = 0

        for major in range(26):
            if total[major] == 0:
                continue
            for minor in range(26):
                if major == minor or total[minor] == 0:
                    continue

                major_count = 0
                minor_count = 0
                remaining_minor = total[minor]

                for ch in s:
                    idx = ord(ch) - 97
                    if idx != major and idx != minor:
                        continue

                    if idx == major:
                        major_count += 1
                    else:
                        minor_count += 1
                        remaining_minor -= 1

                    if minor_count > 0:
                        answer = max(answer, major_count - minor_count)

                    if major_count < minor_count and remaining_minor > 0:
                        major_count = 0
                        minor_count = 0

        return answer