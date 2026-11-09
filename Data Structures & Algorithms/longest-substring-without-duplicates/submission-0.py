class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        longest_str_len = 0
        stored_chars = set()

        for i in range(len(s)):
            while s[i] in stored_chars:
                stored_chars.remove(s[l])
                l += 1
                
            stored_chars.add(s[i])
            str_len = i - l + 1
            longest_str_len = max(longest_str_len, str_len)
        
        return longest_str_len