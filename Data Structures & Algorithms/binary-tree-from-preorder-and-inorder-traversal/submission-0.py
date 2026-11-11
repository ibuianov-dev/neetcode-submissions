# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_map = {val: idx for idx, val in enumerate(inorder)}
        preorder_idx = [0]

        def arr_to_tree(l, r):
            if l > r:
                return None
            root_val = preorder[preorder_idx[0]]
            preorder_idx[0] += 1
            root = TreeNode(root_val)


            root.left = arr_to_tree(l, inorder_map[root_val] - 1)
            root.right = arr_to_tree(inorder_map[root_val] + 1, r)

            return root

        return arr_to_tree(0, len(inorder) - 1)