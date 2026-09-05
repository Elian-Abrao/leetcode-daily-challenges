from typing import List
from collections import defaultdict

class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        # Knows secret initially: person 0 and firstPerson
        knows = [False] * n
        knows[0] = True
        knows[firstPerson] = True
        
        # Group meetings by time to process all meetings at the same time together
        # This is critical: secret can spread instantaneously within the same time
        time_to_meetings = defaultdict(list)
        for x, y, t in meetings:
            time_to_meetings[t].append((x, y))
        
        # Process times in ascending order
        for t in sorted(time_to_meetings.keys()):
            # Build graph for this time slot
            # Only include people who have at least one meeting now
            graph = defaultdict(list)
            participants = set()
            for x, y in time_to_meetings[t]:
                graph[x].append(y)
                graph[y].append(x)
                participants.add(x)
                participants.add(y)
            
            # BFS/DFS from all people who already know the secret
            # among the current participants
            stack = []
            for p in participants:
                if knows[p]:
                    stack.append(p)
            
            # Propagate knowledge within this time slot
            while stack:
                curr = stack.pop()
                for neighbor in graph[curr]:
                    if not knows[neighbor]:
                        knows[neighbor] = True
                        stack.append(neighbor)
        
        # Collect all people who know the secret
        return [i for i in range(n) if knows[i]]