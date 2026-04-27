from typing import List
from collections import deque

class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        # Early exit: if endGene is not in bank, no valid mutation path exists
        bank_set = set(bank)
        if endGene not in bank_set:
            return -1
        
        # BFS to find shortest path from startGene to endGene
        # Each state is a gene string, and edges exist between genes differing by exactly 1 character
        queue = deque([(startGene, 0)])  # (current_gene, mutation_count)
        visited = {startGene}
        genes = ['A', 'C', 'G', 'T']
        
        while queue:
            current_gene, mutations = queue.popleft()
            
            # Check if we've reached the target
            if current_gene == endGene:
                return mutations
            
            # Try all possible single-character mutations
            for i in range(len(current_gene)):
                for gene_char in genes:
                    # Skip if character is the same (no mutation)
                    if gene_char == current_gene[i]:
                        continue
                    
                    # Generate the mutated gene
                    mutated_gene = current_gene[:i] + gene_char + current_gene[i+1:]
                    
                    # Only proceed if this mutation is valid (in bank) and not visited
                    if mutated_gene in bank_set and mutated_gene not in visited:
                        visited.add(mutated_gene)
                        queue.append((mutated_gene, mutations + 1))
        
        # No path found from startGene to endGene
        return -1