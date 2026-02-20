from __future__ import annotations
from typing import List, Any

class Solution:
    def departmentTopThree(self, employees: List[List[Any]], departments: List[List[Any]]) -> List[List[Any]]:
        dept_id_to_name = {}
        if departments:
            for row in departments:
                if len(row) >= 2:
                    dept_id_to_name[row[0]] = row[1]

        by_dept: dict[Any, List[tuple[str, Any]]] = {}
        if employees:
            for row in employees:
                if len(row) < 4:
                    continue
                dept_id = row[3]
                name = row[1]
                salary = row[2]
                if dept_id not in by_dept:
                    by_dept[dept_id] = []
                by_dept[dept_id].append((name, salary))

        result: List[List[Any]] = []
        for dept_id, emps in by_dept.items():
            salaries = sorted({s for _, s in emps}, reverse=True)
            top_salaries = salaries[:3]
            dept_name = dept_id_to_name.get(dept_id, str(dept_id))
            for sal in top_salaries:
                for nm, s in emps:
                    if s == sal:
                        result.append([dept_name, nm, s])

        result.sort(key=lambda x: (x[0], x[1], x[2]))
        return result