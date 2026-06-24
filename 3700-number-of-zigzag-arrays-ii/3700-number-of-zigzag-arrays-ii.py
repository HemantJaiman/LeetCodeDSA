class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        MOD = 10**9 + 7
        
        # Edge cases
        if n == 0: return 0
        if n == 1: return r - l + 1
            
        m = r - l + 1
        
        # 1. Construct the Transition Matrix T of size m x m
        # T[j][k] = 1 if k >= m - j, else 0
        T = [[0] * m for _ in range(m)]
        for j in range(m):
            for k in range(m):
                if k >= m - j:
                    T[j][k] = 1
                    
        # Helper function to multiply two matrices under modulo
        def multiply(A, B):
            C = [[0] * m for _ in range(m)]
            for i in range(m):
                for k in range(m):
                    if A[i][k] == 0: continue
                    for j in range(m):
                        C[i][j] = (C[i][j] + A[i][k] * B[k][j]) % MOD
            return C

        # Helper function to compute (Matrix^power) using binary exponentiation
        def power_matrix(mat, p):
            # Start with Identity Matrix
            res = [[0] * m for _ in range(m)]
            for i in range(m):
                res[i][i] = 1
                
            base = mat
            while p > 0:
                if p % 2 == 1:
                    res = multiply(res, base)
                base = multiply(base, base)
                p //= 2
            return res

        # 2. Raise the transition matrix to the power of (n - 1)
        final_transition = power_matrix(T, n - 1)
        
        # 3. Multiply the final transition matrix by the initial DP vector [1, 1, ..., 1]
        # Since the initial vector is all 1s, the final value at index i is just the sum of row i
        final_dp_sum = 0
        for row in final_transition:
            final_dp_sum = (final_dp_sum + sum(row)) % MOD
            
        # 4. Multiply by 2 to account for both symmetric start paths (UP vs DOWN)
        return (final_dp_sum * 2) % MOD