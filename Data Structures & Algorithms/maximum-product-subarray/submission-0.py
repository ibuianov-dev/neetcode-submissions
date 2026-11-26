class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        min_val = 1
        max_val = 1
        result = max(nums)

        for num in nums:
            if num == 0:
                min_val = 1
                max_val = 1
                continue

            current_min_val = min_val
            min_val = min(num, min_val * num, max_val * num)
            max_val = max(num, current_min_val * num, max_val * num)
            result = max(result, max_val)
        
        return result