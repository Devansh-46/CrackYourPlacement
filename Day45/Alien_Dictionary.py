#Back-end complete function Template for Python 3
class Solution:

    def findOrder(self, dict, n, k):
        graph = {chr(i + 97): [] for i in range(k)}  # first k letters

        for i in range(n - 1):
            for j in range(min(len(dict[i]), len(dict[i + 1]))):
                if dict[i][j] != dict[i + 1][j]:
                    graph[dict[i][j]].append(dict[i + 1][j])
                    break
        # topological sorting of graph nodes
        stack = []
        visited = set()

        def dfs(c):
            if c in visited:
                return
            visited.add(c)
            for adj in graph[c]:
                dfs(adj)
            stack.append(c)

        for c in graph:
            dfs(c)

        stack.reverse()  # reverse the stack for topological order
        order = "".join(stack)
        return order
