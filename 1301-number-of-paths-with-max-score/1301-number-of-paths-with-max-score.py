class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        if not board: return [0,0]
        if board[0][0] != "E" or board[-1][-1] != "S": return [0,0]

        n = len(board)
        MOD = 10**9 + 7
        
        # Cache to store: (r, c) -> [max_score, path_count]
        memo = {}

        def dfs(r, c):
            # Base Case: We successfully reached the destination 'E'
            if r == 0 and c == 0:
                return [0, 1] # [score, path_count]
                
            if (r, c) in memo:
                return memo[(r, c)]

            best_score = -1
            total_paths = 0

            directions = [[-1,0], [0,-1], [-1,-1]]
            for dr, dc in directions:
                next_r, next_c = dr + r, dc + c
                if min(next_r, next_c) < 0 or board[next_r][next_c] == "X":
                    continue

                # Get the optimal result from the neighboring cell
                next_score, next_paths = dfs(next_r, next_c)
                
                # If the neighbor actually has a valid pathway to 'E'
                if next_score != -1:
                    if next_score > best_score:
                        best_score = next_score
                        total_paths = next_paths
                    elif next_score == best_score:
                        total_paths = (total_paths + next_paths) % MOD

            # If no valid path to 'E' could be found from this square
            if best_score == -1:
                memo[(r, c)] = [-1, 0]
                return memo[(r, c)]

            # Convert character to integer value ('S' contributes 0)
            curr_val = 0 if board[r][c] == "S" else int(board[r][c])
            
            # Save the result to cache and return it up
            memo[(r, c)] = [best_score + curr_val, total_paths]
            return memo[(r, c)]
        
        # Start tracking from 'S' (bottom-right corner)
        final_score, final_paths = dfs(n - 1, n - 1)
        
        # If final_score is -1, it means 'E' was completely blocked off
        if final_score == -1:
            return [0, 0]
            
        return [final_score, final_paths]
                