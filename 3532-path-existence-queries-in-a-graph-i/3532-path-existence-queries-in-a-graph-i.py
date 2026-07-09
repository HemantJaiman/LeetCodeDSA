class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        output = []

        groups = [0] * n   # group_id
        curr_group = 0

        for i in range(1, n):
            if nums[i] - nums[i-1] > maxDiff:
                curr_group += 1
            groups[i] = curr_group

        for src, dst in queries:
            output.append(groups[src] == groups[dst])
        return output

