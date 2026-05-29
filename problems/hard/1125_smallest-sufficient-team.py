from typing import List

class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        skill_to_bit = {skill: i for i, skill in enumerate(req_skills)}
        n_skills = len(req_skills)
        target_mask = (1 << n_skills) - 1
        
        people_masks = []
        for person_skills in people:
            mask = 0
            for skill in person_skills:
                if skill in skill_to_bit:
                    mask |= (1 << skill_to_bit[skill])
            people_masks.append(mask)
        
        dp = {0: []}
        
        for person_idx, person_mask in enumerate(people_masks):
            if person_mask == 0:
                continue
            
            current_states = list(dp.items())
            
            for current_mask, current_team in current_states:
                new_mask = current_mask | person_mask
                
                if new_mask == current_mask:
                    continue
                
                new_team = current_team + [person_idx]
                
                if new_mask not in dp or len(new_team) < len(dp[new_mask]):
                    dp[new_mask] = new_team
        
        return dp[target_mask]