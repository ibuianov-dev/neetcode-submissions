class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        for char in bin(n)[2:]:
            if char == '1':
                count += 1

        return count
