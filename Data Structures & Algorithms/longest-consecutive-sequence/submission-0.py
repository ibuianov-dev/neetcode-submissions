class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        longest_sequence = 0

        for num in nums_set:
            if num - 1 not in nums_set:
                sequence_count = 1
                while num + sequence_count in nums_set:
                    sequence_count += 1
                longest_sequence = max(longest_sequence, sequence_count)
        
        return longest_sequence

            