from typing import List

class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        # Since requests.length <= 16, we can try all 2^16 subsets
        # For each subset, check if net change in each building is zero
        # Track the maximum size of valid subsets
        
        m = len(requests)
        max_requests = 0
        
        # Iterate through all possible subsets using bitmask
        # 1 << m gives us 2^m possible combinations
        for mask in range(1 << m):
            # Count net change for each building in this subset
            net_change = [0] * n
            count = 0
            
            # Process each request in the current subset
            for i in range(m):
                # Check if i-th request is included in current subset
                if mask & (1 << i):
                    from_building, to_building = requests[i]
                    net_change[from_building] -= 1  # One employee leaves
                    net_change[to_building] += 1     # One employee arrives
                    count += 1
            
            # Check if all buildings have net zero change
            # This means the subset of requests is achievable
            if all(change == 0 for change in net_change):
                max_requests = max(max_requests, count)
        
        return max_requests