# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        max_depth = 0
        
        def dfs(node, current_depth = 0):
            nonlocal max_depth
            if not node:
                return

            current_depth += 1
            max_depth = max(max_depth, current_depth)
            dfs(node.left, current_depth)
            dfs(node.right, current_depth)

        dfs(root)
        return max_depth