# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # check if current value is less/equal than q and more/equal than p
        # if so then return the node
        # if q is less than current we traverse left
        # if p is more than current we traverse left

        low = min(p.val, q.val)
        high = max(p.val, q.val)

        def traverse(node):
            if node.val >= low and node.val <= high:
                return node
            if high < node.val:
                return traverse(node.left)
            if low > node.val:
                return traverse(node.right)
        
        return traverse(root)