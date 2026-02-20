from __future__ import annotations
from typing import List, Any

class Solution:
    def combineTables(self, Person: List[List[Any]], Address: List[List[Any]]) -> List[List[Any]]:
        # Build mapping from personId to (firstName, lastName)
        person_map = {}
        for row in Person:
            if len(row) >= 3:
                pid, firstName, lastName = row[0], row[1], row[2]
                person_map[pid] = (firstName, lastName)

        # Build mapping from personId to (city, state)
        address_map = {}
        for row in Address:
            if len(row) >= 4:
                _, pid, city, state = row[0], row[1], row[2], row[3]
                address_map[pid] = (city, state)

        # Produce result in the order of Person rows
        result = []
        for row in Person:
            pid = row[0]
            firstName = row[1] if len(row) > 1 else None
            lastName = row[2] if len(row) > 2 else None
            city, state = address_map.get(pid, (None, None))
            result.append([firstName, lastName, city, state])

        return result