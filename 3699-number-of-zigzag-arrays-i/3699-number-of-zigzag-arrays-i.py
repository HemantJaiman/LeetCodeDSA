class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        MOD = 10**9 + 7
        
        if n == 0: return 0
        if n == 1: return r - l + 1
            
        num_values = r - l + 1
        
        # up[v] = valid sequences ending at value 'v' after an UP move
        # down[v] = valid sequences ending at value 'v' after a DOWN move
        up = [0] * num_values
        down = [0] * num_values
        
        # OPTIMIZATION: Eliminate the O((R-L)^2) nested base case loop with linear math!
        for curr in range(num_values):
            up[curr] = curr
            down[curr] = num_values - 1 - curr
                    
        if n == 2:
            return (sum(up) + sum(down)) % MOD
            
        # Process lengths from 3 up to n in strict O(N * (R-L)) time
        for length in range(3, n + 1):
            next_up = [0] * num_values
            next_down = [0] * num_values
            
            # Create a running prefix sum of the 'down' states
            pref_down = [0] * (num_values + 1)
            curr_sum_down = 0
            for i in range(num_values):
                curr_sum_down = (curr_sum_down + down[i]) % MOD
                pref_down[i + 1] = curr_sum_down
                
            # Create a running suffix sum of the 'up' states
            suff_up = [0] * (num_values + 1)
            curr_sum_up = 0
            for i in range(num_values - 1, -1, -1):
                curr_sum_up = (curr_sum_up + up[i]) % MOD
                suff_up[i] = curr_sum_up
            
            # Build the state transitions instantly
            for i in range(num_values):
                next_up[i] = pref_down[i]
                next_down[i] = suff_up[i + 1]
                
            up = next_up
            down = next_down
            
        return (sum(up) + sum(down)) % MOD
                