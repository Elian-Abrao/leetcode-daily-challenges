from typing import List
import heapq

class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        # Create a list of critical events (x-coordinate, event type, height)
        # Event type: 0 for building start (processed first), 1 for building end
        events = []
        for left, right, height in buildings:
            # Use negative height for start events to prioritize taller buildings
            # when multiple buildings start at the same x-coordinate
            events.append((left, 0, height))
            events.append((right, 1, height))
        
        # Sort events by x-coordinate, then by event type (start before end),
        # then by height (taller first for starts, shorter first for ends)
        events.sort(key=lambda x: (x[0], x[1], -x[2] if x[1] == 0 else x[2]))
        
        result = []
        # Max heap to track active building heights (use negative for max heap)
        active_heights = [0]  # Ground level is always present
        
        i = 0
        while i < len(events):
            curr_x = events[i][0]
            
            # Process all events at the same x-coordinate
            while i < len(events) and events[i][0] == curr_x:
                x, event_type, height = events[i]
                
                if event_type == 0:  # Building start
                    heapq.heappush(active_heights, -height)
                else:  # Building end
                    # Remove the height from active set
                    # Note: we can't efficiently remove from heap, so we use lazy deletion
                    active_heights.remove(-height)
                    heapq.heapify(active_heights)
                
                i += 1
            
            # The current max height after processing all events at curr_x
            max_height = -active_heights[0]
            
            # Add key point only if height changes
            if not result or result[-1][1] != max_height:
                result.append([curr_x, max_height])
        
        return result