class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        sequence_lengths = [1] * len(nums)
        
        for i in range(len(nums) - 1, -1, -1):
            for j in range(i, len(nums)):
                if nums[i] < nums[j]:
                    sequence_lengths[i] = max(sequence_lengths[i], 1 + sequence_lengths[j])
        
        return max(sequence_lengths)
