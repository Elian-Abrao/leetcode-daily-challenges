from __future__ import annotations
from typing import List

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        # Map each employee ID to their Employee object for O(1) lookup.
        employee_by_id = {employee.id: employee for employee in employees}

        total_importance = 0
        # Iterative DFS avoids Python recursion limits on deep chains.
        stack = [id]

        while stack:
            employee = employee_by_id[stack.pop()]
            total_importance += employee.importance

            # Push direct subordinates; their own subordinates are processed later.
            stack.extend(employee.subordinates)

        return total_importance