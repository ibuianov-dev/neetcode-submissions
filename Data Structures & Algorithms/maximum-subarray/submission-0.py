class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        max_num = max(nums)
        if max_num <= 0:
            return max_num

        max_sum = 0
        current_sum = 0

        for num in nums:
            current_sum += num
            if current_sum < 0:
                current_sum = 0
                continue
            max_sum = max(max_sum, current_sum)

        return max_sum

