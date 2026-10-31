class Solution:
    def subdomainVisits(self, cpdomains: list[str]) -> list[str]:
        # Use Counter to accumulate visits for each subdomain
        from collections import Counter
        counter = Counter()

        for entry in cpdomains:
            # Split "count domain"
            count_str, domain = entry.split()
            count = int(count_str)

            # Break domain into parts (e.g., ["discuss","leetcode","com"])
            parts = domain.split('.')

            # All suffixes: for each starting index i, the subdomain is parts[i:]
            for i in range(len(parts)):
                sub = '.'.join(parts[i:])
                counter[sub] += count

        # Build output list in any order
        return [f"{cnt} {dom}" for dom, cnt in counter.items()]