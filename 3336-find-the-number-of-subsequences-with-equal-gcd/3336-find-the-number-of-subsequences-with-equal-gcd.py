class Solution:
    def subsequencePairCount(self, nums: List[int]) -> int:
        MOD = 1_000_000_007
        n = len(nums)
        
        # We memoize based on (index, GCD of Team 1, GCD of Team 2)
        @lru_cache(None)
        def dp(i: int, x: int, y: int) -> int:
            # Base Case: All elements processed
            if i == n:
                # Both teams must be non-empty (x > 0, y > 0) and have equal GCDs
                return 1 if (x > 0 and x == y) else 0
            
            curr_val = nums[i]
            
            # Option 1: Skip the current number
            skip = dp(i + 1, x, y)
            
            # Option 2: Put the current number into Subsequence 1 (Team 1)
            # If Team 1 is empty (x == 0), the new GCD is simply curr_val.
            new_x = curr_val if x == 0 else math.gcd(x, curr_val)
            take1 = dp(i + 1, new_x, y)
            
            # Option 3: Put the current number into Subsequence 2 (Team 2)
            # If Team 2 is empty (y == 0), the new GCD is simply curr_val.
            new_y = curr_val if y == 0 else math.gcd(y, curr_val)
            take2 = dp(i + 1, x, new_y)
            
            # Return the sum of all valid options modulo 10^9 + 7
            return (skip + take1 + take2) % MOD
            
        # Start at index 0, with both subsequence GCDs initialized to 0 (empty state)
        return dp(0, 0, 0)