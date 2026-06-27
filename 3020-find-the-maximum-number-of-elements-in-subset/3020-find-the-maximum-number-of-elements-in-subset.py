class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        nums_map = Counter(nums)

        res = 1
        if 1 in nums_map:
            if nums_map[1] % 2 == 0:
                res = max(res, nums_map[1]-1)
            else:
                res = nums_map[1]
        
        for n in nums_map:
            if n == 1:
                continue
            
            curr_n = n
            curr_len = 0

            while True:
                # checking the value with 2 encounters
                if nums_map[curr_n] > 1:
                    curr_len += 2
                    curr_n *= curr_n
                elif nums_map[curr_n] == 1:
                    curr_len += 1
                    break
                # Condition 3: Element is missing; turn the last side element into the peak
                else:
                    curr_len -= 1
                    break
            
            res = max(res, curr_len)
        return res

            