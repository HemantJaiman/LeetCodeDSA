class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        visit = set()
        Rows, Cols = len(grid), len(grid[0])

        def dfs(r,c,health):
            
            if min(r,c) < 0 or r>=Rows or c>= Cols or (r,c,health) in visit or health < 1:
                return False

            visit.add((r,c, health))

            if grid[r][c] == 1:
                health -=1

            if r== Rows-1 and c==Cols-1:
                return health >= 1

            if dfs(r+1, c, health) or dfs(r-1,c,health) or dfs(r,c+1,health) or dfs(r,c-1,health):
                return True
            
            return False

        return dfs(0,0,health)