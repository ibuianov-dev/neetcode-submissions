class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        results = []

        def dfs(i, current_sum, curr_list):
            if i >= len(nums):
                return
            if current_sum == target:
                results.append(curr_list.copy())
                return
            if current_sum > target:
                return
            
            curr_list.append(nums[i])
            dfs(i, current_sum + nums[i], curr_list)
            curr_list.pop()
            dfs(i + 1, current_sum, curr_list)

        dfs(0, 0, [])
        return results