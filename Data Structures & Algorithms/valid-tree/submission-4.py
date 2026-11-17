class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n:
            return True

        adj_list = { i: [] for i in range(n)}
        seen_nodes = set()

        for n1, n2 in edges:
            adj_list[n1].append(n2)
            adj_list[n2].append(n1)

        def dfs(i, previous):
            if i in seen_nodes:
                return False
            seen_nodes.add(i)

            for neigbhor in adj_list[i]:
                if neigbhor == previous:
                    continue
                if not dfs(neigbhor, i):
                    return False

            return True

        return dfs(0, -1) and n == len(seen_nodes)
