class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        nums_len = len(nums)
        prefix = [1] * nums_len
        postfix = [1] * nums_len

        for i in range(1, nums_len):
            prefix[i] = prefix[i - 1] * nums[i - 1]
        for i in range(nums_len - 2, -1, -1):
            postfix[i] = postfix[i + 1] * nums[i + 1]

        result = [1] * nums_len
        for i in range(nums_len):
            result[i] = prefix[i] * postfix[i]

        return result