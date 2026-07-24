class Solution:
    def maxPathScore(self, grid: List[List[int]], k: int) -> int:
        Rows, Cols = len(grid), len(grid[0])
        
        # dp[r][c][cost] = max score reached at (r, c) with exact 'cost'
        dp = [[[-1] * (k + 1) for _ in range(Cols)] for _ in range(Rows)]

        def get_info(v):
            return v, (1 if v > 0 else 0)

        s0, c0 = get_info(grid[0][0])
        if c0 <= k:
            dp[0][0][c0] = s0

        for r in range(Rows):
            for c in range(Cols):
                for cost in range(k + 1):
                    if dp[r][c][cost] == -1:
                        continue
                    
                    curr_score = dp[r][c][cost]

                    # Move Right
                    if c + 1 < Cols:
                        s, c_cost = get_info(grid[r][c + 1])
                        if cost + c_cost <= k:
                            dp[r][c + 1][cost + c_cost] = max(dp[r][c + 1][cost + c_cost], curr_score + s)

                    # Move Down
                    if r + 1 < Rows:
                        s, c_cost = get_info(grid[r + 1][c])
                        if cost + c_cost <= k:
                            dp[r + 1][c][cost + c_cost] = max(dp[r + 1][c][cost + c_cost], curr_score + s)

        ans = max(dp[Rows - 1][Cols - 1])
        return ans if ans != -1 else -1