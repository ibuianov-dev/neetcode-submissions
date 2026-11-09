class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        stored_chars = {}
        l = 0
        max_len = 0

        for i in range(len(s)):
            if s[i] not in stored_chars:
                stored_chars[s[i]] = 0
            stored_chars[s[i]] += 1

            max_val = max(stored_chars.values())
            while (i - l + 1) - max_val > k:
                stored_chars[s[l]] -= 1
                l += 1
                max_val = max(stored_chars.values())

            max_len = max(max_len, i - l + 1)

        return max_len