class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        output = 0
        n = len(nums)

        for i in range(n):
            if n % (i+1) == 0:
                output += nums[i] ** 2
        
        return output