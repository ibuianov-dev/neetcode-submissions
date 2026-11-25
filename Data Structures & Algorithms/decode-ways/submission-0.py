class Solution:
    def numDecodings(self, s: str) -> int:
        seen_combintaions = {}

        def dfs(start_idx):
            if start_idx in seen_combintaions:
                return seen_combintaions[start_idx]

            if start_idx == len(s):
                return 1

            if s[start_idx] == '0':
                return 0

            total = dfs(start_idx + 1)

            if start_idx + 1 < len(s) and int(s[start_idx:start_idx + 2]) <= 26:
                total += dfs(start_idx + 2)

            seen_combintaions[start_idx] = total
            return total

        return dfs(0)