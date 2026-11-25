class Solution:
    def countSubstrings(self, s: str) -> int:
        palindrome_count = 0

        def outerPalindromeExpand(left, right):
            nonlocal palindrome_count

            while left >= 0 and right < len(s) and s[left] == s[right]:
                palindrome_count += 1
                left -= 1
                right += 1

        for i in range(len(s)):
            outerPalindromeExpand(i, i)
            outerPalindromeExpand(i, i + 1)

        return palindrome_count