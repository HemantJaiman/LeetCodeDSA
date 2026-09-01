class UnionFind:
    def __init__(self, n):
        self.parents= [i for i in range(n+1)]
        self.ranks = [1] * (n+1)
    
    def find(self, node):
        parent = self.parents[node]

        while parent != self.parents[parent]:
            self.parents[parent] = self.parents[self.parents[parent]]
            parent = self.parents[parent]
        return parent

    def union(self, node1, node2):
        parent1,parent2 = self.find(node1), self.find(node2)

        if parent1 == parent2:
            return False
        
        if self.ranks[parent1] >= self.ranks[parent2]:
            self.ranks[parent1] += self.ranks[parent2]
            self.parents[node2] = parent1
        else:
            self.ranks[parent2] += self.ranks[parent1]
            self.parents[node1] = parent2

        return True


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        uf = UnionFind(len(edges))
        output = []
        for node1, node2 in edges:
            if not uf.union(node1,node2):
                output = [node1,node2]
        
        return output

        