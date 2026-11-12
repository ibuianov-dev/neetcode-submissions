# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        max_val = [root.val]

        def traverse(node):
            if not node:
                return 0
            
            left_max = max(0, traverse(node.left))
            right_max = max(0, traverse(node.right))
            current_sum = left_max + right_max + node.val
            max_val[0] = max(max_val[0], current_sum)

            return node.val + max(left_max, right_max)

        traverse(root)
        return max_val[0]