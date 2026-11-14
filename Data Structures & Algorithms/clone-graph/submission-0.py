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
        nodes_map = {}
        seen_roots = set()
        queue = deque([node])

        while queue:
            current = queue.popleft()
            if current in seen_roots:
                continue
            seen_roots.add(current)

            if current not in nodes_map:
                nodes_map[current] = Node(current.val)
            
            current_neigbors = []

            for neigbor in current.neighbors:
                if neigbor not in nodes_map:
                    nodes_map[neigbor] = Node(neigbor.val)
                current_neigbors.append(nodes_map[neigbor])
                queue.append(neigbor)

            nodes_map[current].neighbors = current_neigbors

        return nodes_map[node]

