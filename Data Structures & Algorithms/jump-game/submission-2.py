class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # [1,2,0,1,0]

        # [1,2,0,1,0]
        #    i

        stored_idx = set()

        def canReach(idx):
            if idx == len(nums) - 1:
                return True
            if idx in stored_idx or idx >= len(nums):
                return False
            if nums[idx] == 0:
                return False

            stored_idx.add(idx)
            
            for i in range(1, min(nums[idx] + 1, len(nums))):
                if canReach(idx + i):
                    return True
            
            return False
            
        return canReach(0)
