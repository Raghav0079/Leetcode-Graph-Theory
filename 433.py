'''
A gene string can be represented by an 8-character long string, with choices from 'A', 'C', 'G', and 'T'.

Suppose we need to investigate a mutation from a gene string startGene to a gene string endGene where one mutation is defined as one single character changed in the gene string.

For example, "AACCGGTT" --> "AACCGGTA" is one mutation.
There is also a gene bank bank that records all the valid gene mutations. A gene must be in bank to make it a valid gene string.

Given the two gene strings startGene and endGene and the gene bank bank, return the minimum number of mutations needed to mutate from startGene to endGene. If there is no such a mutation, return -1.

Note that the starting point is assumed to be valid, so it might not be included in the bank.
'''
from collections import deque

class Solution(object):
    def minMutation(self, startGene, endGene, bank):
        """
        :type startGene: str
        :type endGene: str
        :type bank: List[str]
        :rtype: int
        """
        bank = set(bank) # O(1) lookup
        if endGene not in bank:
            return -1
        
        queue = deque([(startGene, 0)])
        # Use a set to track visited genes to prevent infinite loops
        visited = {startGene}
        
        while queue:
            current, steps = queue.popleft()
            
            if current == endGene:
                return steps
            
            # Try changing each character of the gene
            for i in range(len(current)):
                for char in "ACGT":
                    mutation = current[:i] + char + current[i+1:]
                    
                    if mutation in bank and mutation not in visited:
                        visited.add(mutation)
                        queue.append((mutation, steps + 1))
        
        return -1
