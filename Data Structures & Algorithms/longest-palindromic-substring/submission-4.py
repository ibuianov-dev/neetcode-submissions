class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_len = 0
        max_palindrome = (0,0)     

        def expandPalindrome(left, right):
            nonlocal max_palindrome, max_len
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if max_len < right - left + 1:
                    max_palindrome = (left, right)
                    max_len = right - left + 1
                left -= 1
                right += 1

        for i in range(len(s)):
            expandPalindrome(i, i)
            expandPalindrome(i, i + 1)

        if max_len == 0:
            return ""
        
        return s[max_palindrome[0]:max_palindrome[1] + 1]
        