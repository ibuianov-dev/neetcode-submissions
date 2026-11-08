class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_counter = Counter(nums)
        heap_counter = [(-v, k) for k, v in nums_counter.items()]
        heapq.heapify(heap_counter)

        result = []
        for i in range(k):
            top = heapq.heappop(heap_counter)[1]
            result.append(top)

        return result