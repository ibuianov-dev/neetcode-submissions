class MedianFinder:

    def __init__(self):
        self.small_heap = [] # max heap
        self.large_heap = [] # min heap

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small_heap, num * -1)

        if (self.small_heap and self.large_heap) and self.small_heap[0] * -1 > self.large_heap[0]:
            val = heapq.heappop(self.small_heap) * -1
            heapq.heappush(self.large_heap, val)
        
        if len(self.small_heap) > len(self.large_heap) + 1:
            val = heapq.heappop(self.small_heap) * -1
            heapq.heappush(self.large_heap, val)
        elif len(self.small_heap) < len(self.large_heap):
            val = heapq.heappop(self.large_heap) * -1
            heapq.heappush(self.small_heap, val)

    def findMedian(self) -> float:
        if len(self.small_heap) > len(self.large_heap):
            return self.small_heap[0] * -1
        
        return (-1 * self.small_heap[0] + self.large_heap[0]) / 2


        