class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        if k<= 0 or not nums:
            return 0

        longest_good_subarray = 0
        curr_freq_map = {}
        left = 0

        for right in range(0,len(nums)):
            curr_freq_map[nums[right]] = curr_freq_map.get(nums[right], 0) + 1
            
            while curr_freq_map[nums[right]] > k and left <= right:
                curr_freq_map[nums[left]] -= 1
                left += 1
            
    
            longest_good_subarray = max(longest_good_subarray, right-left + 1)
        
        return longest_good_subarray