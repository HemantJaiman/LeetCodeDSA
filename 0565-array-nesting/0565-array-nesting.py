class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        output = 0
        n_set = set()
        for i in range(len(nums)):
            
            curr = 0
            while nums[i] not in n_set:
                curr += 1
                n_set.add(nums[i])
                i = nums[i]
            
            output = max(output, curr)
        
        return output