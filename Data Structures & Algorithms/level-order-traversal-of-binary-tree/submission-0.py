# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        results = [[root]]

        while len(results[-1]) > 0:
            new_level = []

            for node in results[-1]:
                if node.left:
                    new_level.append(node.left)
                if node.right:
                    new_level.append(node.right)
            
            results.append(new_level)

        results.pop()
        for i in range(len(results)):
            for j in range(len(results[i])):
                results[i][j] = results[i][j].val

        return results

