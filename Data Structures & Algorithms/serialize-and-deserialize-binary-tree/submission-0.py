# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        queue = deque([root])
        level_order = []

        while queue:
            current = queue.pop()
            
            if current:
                level_order.append(current.val)
                queue.appendleft(current.left)
                queue.appendleft(current.right)
            else:
                level_order.append(None)
        
        while level_order and level_order[-1] is None:
            level_order.pop()

        return '#'.join([str(val) if val is not None else 'null' for val in level_order])
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data:
            return None

        level_order = data.split('#')
        level_order = [int(val) if val != 'null' else None for val in level_order]

        root = TreeNode(level_order[0])
        queue = deque([root])
        i = 1

        while queue and i < len(level_order):
            current = queue.popleft()

            if i < len(level_order) and level_order[i] is not None:
                current.left = TreeNode(level_order[i])
                queue.append(current.left)
            i += 1

            if i < len(level_order) and level_order[i] is not None:
                current.right = TreeNode(level_order[i])
                queue.append(current.right)
            i += 1

        return root

        


