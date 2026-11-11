# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def traverse(node, left_boundry = float('-inf'), right_boundry = float('inf')):
            if not node:
                return True
            if node.val >= right_boundry or node.val <= left_boundry:
                return False
            
            return traverse(node.left, left_boundry, node.val) and traverse(node.right, node.val, right_boundry)

        return traverse(root)