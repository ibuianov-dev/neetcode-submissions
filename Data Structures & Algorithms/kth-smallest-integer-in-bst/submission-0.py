# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        min_heap = []
        queue = deque([root])
        
        while queue:
            current = queue.popleft()
            heapq.heappush(min_heap, current.val)

            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)

        for _ in range(k - 1):
            heapq.heappop(min_heap)

        return heapq.heappop(min_heap)
