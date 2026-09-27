class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        nums_set = set(nums)
        max_length = 0
        for n in nums_set:
            if n-1 in nums_set:
                continue
            length = 1
            while n+1 in nums_set:
                length += 1
                n+= 1
            max_length = max(length, max_length)
        
        return max_length