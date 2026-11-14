class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reach = 0

        for i in range(len(nums) - 1):
            if i > max_reach:
                return False

            current_reach = i + nums[i]
            max_reach = max(max_reach, current_reach)

            if current_reach >= len(nums) - 1:
                return True
        
        return max_reach >= len(nums) - 1


