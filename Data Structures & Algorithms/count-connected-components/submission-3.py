class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj_list = {i: [] for i in range(n)}
        seen_values = set()
        count = 0

        for node1, node2 in edges:
            adj_list[node1].append(node2)
            adj_list[node2].append(node1)

        def dfs(node, previous):
            seen_values.add(node)

            for neigbhor in adj_list[node]:
                if neigbhor == previous:
                    continue
                if neigbhor not in seen_values:
                    dfs(neigbhor, node)
            
        for node in range(n):
            if node not in seen_values:
                dfs(node, -1)
                count += 1

        return count