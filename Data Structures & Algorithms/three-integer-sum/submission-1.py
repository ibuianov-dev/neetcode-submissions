class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        triplets = []

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            target = nums[i] * -1
            l = i + 1
            r = len(nums) - 1

            while l < r:
                p_sum = nums[l] + nums[r]
                if p_sum < target:
                    l += 1
                elif p_sum > target:
                    r -= 1
                else:
                    triplets.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1

        return triplets



