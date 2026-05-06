from typing import List
from collections import deque, defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # This is a cycle detection problem in a directed graph
        # If there's a cycle in the prerequisite graph, we cannot finish all courses
        # We use Kahn's algorithm (topological sort with BFS) to detect cycles
        
        # Build adjacency list: graph[b] = list of courses that depend on b
        graph = defaultdict(list)
        # Track in-degree (number of prerequisites) for each course
        in_degree = [0] * numCourses
        
        # Build the graph from prerequisites
        for course, prereq in prerequisites:
            graph[prereq].append(course)
            in_degree[course] += 1
        
        # Initialize queue with all courses that have no prerequisites
        # These can be taken immediately
        queue = deque()
        for course in range(numCourses):
            if in_degree[course] == 0:
                queue.append(course)
        
        # Count how many courses we can complete
        completed = 0
        
        # Process courses in topological order
        while queue:
            # Take a course that has all prerequisites satisfied
            current = queue.popleft()
            completed += 1
            
            # For each course that depends on the current course
            for neighbor in graph[current]:
                # Reduce its in-degree (one prerequisite satisfied)
                in_degree[neighbor] -= 1
                # If all prerequisites are now satisfied, add to queue
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        
        # If we completed all courses, there's no cycle
        # If we couldn't complete all courses, there must be a cycle
        return completed == numCourses