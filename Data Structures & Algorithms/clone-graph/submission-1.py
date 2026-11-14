"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""


class Solution:
    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        if not node:
            return None

        nodes_map = {node: Node(node.val)}
        queue = deque([node])

        while queue:
            current = queue.popleft()

            for neigbor in current.neighbors:
                if neigbor not in nodes_map:
                    nodes_map[neigbor] = Node(neigbor.val)
                    queue.append(neigbor)

                nodes_map[current].neighbors.append(nodes_map[neigbor])

        return nodes_map[node]

