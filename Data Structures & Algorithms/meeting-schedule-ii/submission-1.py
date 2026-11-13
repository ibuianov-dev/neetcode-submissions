"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if len(intervals) < 2:
            return len(intervals)

        intervals.sort(key=lambda interval: interval.start)
        rooms_heap = [intervals[0].end]

        for i in range(1, len(intervals)):
            current_interval = intervals[i]
            if current_interval.start >= rooms_heap[0]:
                heapq.heappop(rooms_heap)

            heapq.heappush(rooms_heap, current_interval.end)

        return len(rooms_heap)


# [(1,5),(5,10),(10,15),(15,20)]
