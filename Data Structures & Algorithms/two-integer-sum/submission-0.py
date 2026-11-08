class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen_values = {}

        for i in range(len(nums)):
            delta = target - nums[i]
            if delta in seen_values:
                return [seen_values[delta], i]
            seen_values[nums[i]] = i
        
        return [-1]