class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        
        # The first element must be 1
        max_val = 1
        
        # Step 2: Check each subsequent element starting from index 1
        for i in range(1, len(arr)):
            # If the current element is large enough to sustain a step up
            if arr[i] >= max_val + 1:
                max_val += 1
                
        return max_val