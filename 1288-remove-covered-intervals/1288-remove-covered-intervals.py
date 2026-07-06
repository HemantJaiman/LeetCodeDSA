class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        output = 0

        last_interval_end = -1

        intervals.sort(key = lambda x: (x[0], -x[1]))

        for start,end in intervals:
            if end <= last_interval_end:
                continue
            else:
                output += 1
                last_interval_end = end
        
        return output