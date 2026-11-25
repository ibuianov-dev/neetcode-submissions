class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
            
        def sub_rob(start_idx, end_idx):
            rob1, rob2 = 0, 0

            for i in range(start_idx, end_idx):
                current = max(rob1 + nums[i], rob2)
                rob1 = rob2
                rob2 = current
        
            return rob2

        return max(sub_rob(0, len(nums) - 1), sub_rob(1, len(nums)))