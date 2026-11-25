class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        past_past_max = 0
        past_max = nums[0]
        max_val = past_max

        for i in range(1, len(nums)):
            current = nums[i] + past_past_max
            max_val = max(current, max_val)

            past_past_max = max(past_past_max, past_max)
            past_max = max(current, past_max)

        return max_val
