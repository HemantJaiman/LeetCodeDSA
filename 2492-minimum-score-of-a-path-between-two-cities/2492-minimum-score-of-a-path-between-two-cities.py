class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        
        # Step 1: Build the bidirectional adjacency list
        adj_list = {i: [] for i in range(1, n + 1)}
        for src, dst, distance in roads:
            adj_list[src].append((dst, distance))
            adj_list[dst].append((src, distance))

        visit = set()
        self.min_score = float("inf")

        # Step 2: Define the DFS traversal
        def dfs(node):
            # Mark the current node as visited
            visit.add(node)
            
            # Explore all roads connected to this city
            for neighbor, distance in adj_list[node]:
                # Track the absolute minimum road distance seen anywhere in this component
                self.min_score = min(self.min_score, distance)
                
                # If the neighboring city hasn't been visited, traverse into it
                if neighbor not in visit:
                    dfs(neighbor)

        # Start DFS from City 1
        dfs(1)
        
        return self.min_score