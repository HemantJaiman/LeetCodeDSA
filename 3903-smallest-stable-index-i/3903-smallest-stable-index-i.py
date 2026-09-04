class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        smallest = float("inf")
        max_val = float("-inf")

        for i in range(len(nums)):
            max_val = max(max_val, nums[i])

            if max_val - min(nums[i:]) <=k:
                smallest = min(smallest, i)


        return -1 if smallest == float("inf") else smallest