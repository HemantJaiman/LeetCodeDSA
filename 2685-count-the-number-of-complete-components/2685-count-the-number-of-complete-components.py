class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        # STEP 1: Build the Adjacency List
        adj_list = {i: [] for i in range(n)}
        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)
            
        visited = set()
        complete_components = 0
        
        # STEP 2: Loop through every node to find all components
        for i in range(n):
            if i in visited:
                continue
                
            # We found a new, unvisited component! Let's explore it using BFS
            queue = deque([i])
            visited.add(i)
            
            vertex_count = 0
            edge_count = 0
            
            # STEP 3: Traverse the component and count vertices and edges
            while queue:
                curr = queue.popleft()
                vertex_count += 1
                
                # Add up the number of neighbors this node has
                edge_count += len(adj_list[curr])
                
                for neighbor in adj_list[curr]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)
            
            # STEP 4: Verify if the component is complete
            # Total degrees in a complete graph must equal V * (V - 1)
            if edge_count == vertex_count * (vertex_count - 1):
                complete_components += 1
                
        return complete_components