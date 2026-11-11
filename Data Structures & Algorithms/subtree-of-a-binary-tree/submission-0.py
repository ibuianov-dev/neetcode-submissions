# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSubroot(root_node, subroot_node):
            if root_node is None and subroot_node is None:
                return True
            if root_node is None or subroot_node is None:
                return False
            if root_node.val != subroot_node.val:
                return False
            
            return isSubroot(root_node.left, subroot_node.left) and isSubroot(root_node.right, subroot_node.right)

        def check_subroot(node):
            if node is None:
                return False
            if isSubroot(node, subRoot):
                return True
            
            return check_subroot(node.left) or check_subroot(node.right)

        return check_subroot(root)