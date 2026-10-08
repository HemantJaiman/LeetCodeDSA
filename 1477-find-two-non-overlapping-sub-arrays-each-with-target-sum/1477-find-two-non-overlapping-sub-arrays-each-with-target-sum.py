class Solution:
    def minSumOfLengths(self, arr: list[int], target: int) -> int:
        best = [float("inf")] * len(arr)

        left= 0
        running_sum = 0

        minimum_len = float("inf")
        output = float("inf")
    
        for right in range(len(arr)):
            running_sum += arr[right]

            while running_sum > target:
                running_sum -= arr[left]
                left += 1
            
            if running_sum == target:
                if left > 0 and best[left-1] != float("inf"):
                    output = min(output, best[left-1] + (right-left + 1))
                minimum_len = min(minimum_len, right-left + 1)
            best[right] = minimum_len
        return output if output != float("inf") else -1 
