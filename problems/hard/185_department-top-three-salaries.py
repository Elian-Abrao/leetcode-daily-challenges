from __future__ import annotations
from typing import List

class Solution:
    def departmentTopThreeSalaries(self, Employee: List[List], Department: List[List]) -> List[List]:
        # Build a mapping from department id to department name
        # Department table format: [id, name]
        dept_map = {dep_id: dep_name for dep_id, dep_name in Department}
        
        # Collect records as (department_name, employee_name, salary)
        records: List[tuple[str, str, int]] = []
        for emp in Employee:
            # Expecting: [id, name, salary, departmentId]
            if len(emp) < 4:
                continue  # skip malformed rows
            emp_id, name, salary, departmentId = emp
            dept_name = dept_map.get(departmentId)
            if dept_name is None:
                continue  # skip employees with unknown department
            records.append((dept_name, name, int(salary)))
        
        # Group employees by department
        from collections import defaultdict
        dept_to_employees: defaultdict[str, List[tuple[str, int]]] = defaultdict(list)
        for dept_name, name, salary in records:
            dept_to_employees[dept_name].append((name, salary))
        
        # For each department, compute top 3 unique salaries and select matching employees
        result: List[List] = []
        for dept_name, items in dept_to_employees.items():
            # items: list of (employee_name, salary) within this department
            unique_salaries = sorted({sal for _, sal in items}, reverse=True)
            top3 = set(unique_salaries[:3])  # top three unique salaries (may be fewer than 3)
            for name, sal in items:
                if sal in top3:
                    result.append([dept_name, name, int(sal)])
        
        # Optional: sort for deterministic output (department, salary desc, name asc)
        result.sort(key=lambda x: (x[0], -x[2], x[1]))
        return result