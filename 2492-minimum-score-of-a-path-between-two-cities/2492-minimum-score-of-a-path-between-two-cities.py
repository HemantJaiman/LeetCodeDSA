class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        
        # Step 1: Build the bidirectional adjacency list
        adj_list = {i: [] for i in range(1, n + 1)}
        for src, dst, distance in roads:
            adj_list[src].append((dst, distance))
            adj_list[dst].append((src, distance))

        # Step 2: Use BFS to explore the entire connected component containing City 1
        queue = deque([1])
        visit = set([1])
        min_score = float("inf")

        while queue:
            curr = queue.popleft()
            
            # Check all roads connected to the current city
            for neighbor, distance in adj_list[curr]:
                # Track the absolute minimum road distance seen anywhere in this component
                min_score = min(min_score, distance)
                
                # Standard BFS tracking: only visit unvisited cities
                if neighbor not in visit:
                    visit.add(neighbor)
                    queue.append(neighbor)

        return min_score