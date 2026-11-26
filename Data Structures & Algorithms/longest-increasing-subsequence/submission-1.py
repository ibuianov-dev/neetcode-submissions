import bisect

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        piles = []
        
        for num in nums:
            insert_idx = bisect.bisect_left(piles, num)
            if insert_idx == len(piles):
                piles.append(num)
            else:
                piles[insert_idx] = num
        
        return len(piles)