class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen_values = set()

        for num in nums:
            if num in seen_values:
                return True
            seen_values.add(num)

        return False