# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSubroot(root_node, subroot_node):
            if not root_node and not subroot_node:
                return True
            if not root_node or not subroot_node:
                return False
            if root_node.val != subroot_node.val:
                return False
            
            return isSubroot(root_node.left, subroot_node.left) and isSubroot(root_node.right, subroot_node.right)

        def check_subroot(node):
            if not node:
                return False
            if isSubroot(node, subRoot):
                return True
            
            return check_subroot(node.left) or check_subroot(node.right)

        return check_subroot(root)