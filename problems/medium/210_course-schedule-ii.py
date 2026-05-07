from typing import List
from collections import deque, defaultdict

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Build adjacency list: course -> list of courses that depend on it
        graph = defaultdict(list)
        # Track in-degree (number of prerequisites) for each course
        in_degree = [0] * numCourses
        
        # Construct graph and in-degree array
        # prerequisites[i] = [a, b] means b -> a (b must be taken before a)
        for course, prereq in prerequisites:
            graph[prereq].append(course)
            in_degree[course] += 1
        
        # Initialize queue with all courses that have no prerequisites
        # These can be taken immediately
        queue = deque()
        for course in range(numCourses):
            if in_degree[course] == 0:
                queue.append(course)
        
        # Result list to store topological order
        order = []
        
        # Kahn's algorithm: BFS-based topological sort
        while queue:
            # Take a course with no remaining prerequisites
            current = queue.popleft()
            order.append(current)
            
            # For each course that depends on the current course
            for neighbor in graph[current]:
                # Reduce its in-degree (one prerequisite satisfied)
                in_degree[neighbor] -= 1
                # If all prerequisites are now satisfied, add to queue
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        
        # If we processed all courses, return the order
        # Otherwise, there's a cycle and it's impossible to complete all courses
        return order if len(order) == numCourses else []