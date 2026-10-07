class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        min_elem = float("inf")
        max_elem = float("-inf")

        for n in nums:
            min_elem = min(n, min_elem)
            max_elem = max(n, max_elem)

        nums_set = set(nums)
        output = []

        for val in range(min_elem+1, max_elem):
            if val not in nums_set:
                output.append(val)
        return output
        