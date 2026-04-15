from __future__ import annotations

from typing import List, Dict
from collections import defaultdict


class Solution:
    def departmentHighestSalary(self, Employee: List[List], Department: List[List]) -> List[List]:
        """
        Given Employee(id, name, salary, departmentId) and Department(id, name),
        return rows [DepartmentName, EmployeeName, Salary] for employees who have
        the highest salary within each department. A department can have multiple
        employees sharing the max salary; all should be returned.
        """
        # Edge case: no departments or no employees yield empty result
        if not Employee or not Department:
            return []

        # Build mapping from department id to department name
        dept_id_to_name: Dict[int, str] = {}
        for row in Department:
            if len(row) >= 2:
                dept_id, dept_name = row[0], row[1]
                dept_id_to_name[dept_id] = dept_name

        # Group employees by their department
        dept_to_emp: defaultdict[int, List[tuple[str, int]]] = defaultdict(list)
        for row in Employee:
            if len(row) < 4:
                continue  # skip malformed rows
            emp_name = row[1]
            salary = row[2]
            dept_id = row[3]
            if dept_id in dept_id_to_name:
                dept_to_emp[dept_id].append((emp_name, salary))

        # For each department with employees, find the max salary and collect matching employees
        result: List[List] = []
        for dept_id, emp_list in dept_to_emp.items():
            if not emp_list:
                continue
            max_salary = max(s for _, s in emp_list)
            dept_name = dept_id_to_name.get(dept_id)
            if dept_name is None:
                continue  # skip if department name unavailable
            for name, sal in emp_list:
                if sal == max_salary:
                    result.append([dept_name, name, sal])

        return result