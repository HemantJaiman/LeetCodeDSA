class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        queue = deque()
        visit = set()
        Rows,Cols = len(grid), len(grid[0])

        # step 1: calculting minimum distance reqired to reach every point
        for r in range(Rows):
            for c in range(Cols):
                if grid[r][c] == 1:
                    queue.append((r,c))
                    visit.add((r,c))
                    grid[r][c] = 0
                else:
                    grid[r][c] = float("-inf")
        while queue:
            for _ in range(len(queue)):
                row,col = queue.popleft()
                directions = [[0,1], [0,-1], [-1,0], [1,0]]

                for dr,dc in directions:
                    next_row, next_col = row + dr, dc + col
                    if min(next_row, next_col) < 0 or next_row == Rows or next_col == Cols or (next_row, next_col) in visit:
                        continue
                    grid[next_row][next_col] = grid[row][col] + 1
                    visit.add((next_row, next_col))
                    queue.append((next_row, next_col))
        
        # step2: now using dijkstra finding the maximum safest route
        max_heap = [[-grid[0][0], 0,0]]  # [val, 0, 0]
        visit = set()
        safeness_factor = float("-inf")
        
        while max_heap:
            factor, row, col = heapq.heappop(max_heap)
            visit.add((row,col))
            current_path_factor = -factor
            if row == Rows-1 and col == Cols-1:
                return current_path_factor
            directions = [[0,1], [0,-1], [-1,0], [1,0]]
            for dr,dc in directions:
                next_row, next_col = row + dr, dc + col
                if min(next_row, next_col) < 0 or next_row == Rows or next_col == Cols or (next_row, next_col) in visit:
                    continue
                visit.add((next_row, next_col))
                next_path_factor = min(current_path_factor, grid[next_row][next_col])
                heapq.heappush(max_heap, [ -next_path_factor , next_row, next_col])
    
