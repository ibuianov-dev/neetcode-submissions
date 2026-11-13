class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if len(intervals) < 2:
            return 0

        intervals.sort()
        last_end = intervals[0][1]
        overlap_count = 0

        for i in range(1, len(intervals)):
            if last_end > intervals[i][0]:
                overlap_count += 1
                last_end = min(last_end, intervals[i][1])
            else:
                last_end = intervals[i][1]

        return overlap_count


# [[1,100], [2,7], [7,10], [11, 14]]