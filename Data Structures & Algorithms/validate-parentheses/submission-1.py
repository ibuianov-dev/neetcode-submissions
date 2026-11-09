class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {")": "(", "}": "{", "]": "["}
        stack = []

        for p in s:
            if p in pairs:
                if len(stack) > 0 and pairs[p] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(p)
        
        return len(stack) == 0