class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        results = []

        def backtrack(current_sum, arr, arr_idx):
            for i in range(arr_idx, len(nums)):
                new_sum = current_sum + nums[i]
                if new_sum == target:
                    results.append([*arr[:], nums[i]])
                if new_sum < target:
                    arr.append(nums[i])
                    backtrack(new_sum, arr, i)
                    arr.pop()

        backtrack(0, [], 0)
        return results