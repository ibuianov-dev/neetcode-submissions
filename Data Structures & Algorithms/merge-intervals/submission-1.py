class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) < 2:
            return intervals
        
        intervals.sort()
        merged = [intervals[0]]
        print(merged)

        for i in range(1, len(intervals)):
            if intervals[i][0] <= merged[-1][1]:
                merged[-1][1] = max(merged[-1][1], intervals[i][1])
            else:
                merged.append(intervals[i])

        return merged
