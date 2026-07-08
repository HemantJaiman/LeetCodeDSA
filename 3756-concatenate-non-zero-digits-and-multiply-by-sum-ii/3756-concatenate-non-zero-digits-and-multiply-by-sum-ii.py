class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7
        n = len(s)

        # 1. Map original indices to squeezed (non-zero) indices
        # map_idx[i] tells us how many non-zero digits exist BEFORE index i
        map_idx = [0] * (n + 1)
        squeezed_digits = []
        
        for i in range(n):
            map_idx[i + 1] = map_idx[i]
            if s[i] != '0':
                squeezed_digits.append(int(s[i]))
                map_idx[i + 1] += 1

        # 2. Build standard prefix arrays on the squeezed data
        m = len(squeezed_digits)
        pref_sum = [0] * (m + 1)
        pref_val = [0] * (m + 1)
        
        for i in range(m):
            pref_sum[i + 1] = pref_sum[i] + squeezed_digits[i]
            pref_val[i + 1] = (pref_val[i] * 10 + squeezed_digits[i]) % MOD

        # Precompute powers of 10 so we can shift numbers in O(1) time
        pow10 = [1] * (m + 1)
        for i in range(1, m + 1):
            pow10[i] = (pow10[i - 1] * 10) % MOD

        # 3. Answer each query
        output = []
        for l, r in queries:
            l = max(0, l)
            r = min(n - 1, r)
            if l > r:
                output.append(0)
                continue

            # Translate original [l, r] bounds to our squeezed [L, R] bounds
            L = map_idx[l]
            R = map_idx[r + 1]

            # If there are no non-zero numbers in this range, the answer is 0
            if L == R:
                output.append(0)
                continue

            # Calculate digit sum using our standard prefix sum array
            digits_sum = pref_sum[R] - pref_sum[L]

            # Calculate the math value of the substring using our prefix value array
            # Formula: (Value up to R) - (Value up to L shifted right by the window size)
            x = (pref_val[R] - pref_val[L] * pow10[R - L]) % MOD

            # Append final answer
            output.append((x * digits_sum) % MOD)

        return output