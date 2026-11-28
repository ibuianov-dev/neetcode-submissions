class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        stored_idx = {}

        def dfs(text_1_idx, text_2_idx):
            if text_1_idx == len(text1) or text_2_idx == len(text2):
                return 0

            result = 0
            idx_key = (text_1_idx, text_2_idx)
            if idx_key in stored_idx:
                return stored_idx[idx_key]

            if text1[text_1_idx] == text2[text_2_idx]:
                result = 1 + dfs(text_1_idx + 1, text_2_idx + 1)
            else:
                result = max(dfs(text_1_idx + 1, text_2_idx), dfs(text_1_idx, text_2_idx + 1))

            stored_idx[idx_key] = result
            return result
            
        return dfs(0, 0)