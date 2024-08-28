from typing import List

class Solution:
    def __init__(self):
        self.timer = 1

    def dfs(self, node, parent, vis, adj, tin, low, bridges):
        vis[node] = 1
        tin[node] = low[node] = self.timer
        self.timer += 1

        for neighbor in adj[node]:
            if neighbor == parent:
                continue
            if vis[neighbor] == 0:
                self.dfs(neighbor, node, vis, adj, tin, low, bridges)
                low[node] = min(low[neighbor], low[node])

                if low[neighbor] > tin[node]:
                    bridges.append([neighbor, node])
            else:
                low[node] = min(low[node], low[neighbor])

    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        adj = [[] for _ in range(n)]
        for u, v in connections:
            adj[u].append(v)
            adj[v].append(u)

        vis = [0] * n
        tin = [float('inf')] * n
        low = [float('inf')] * n
        bridges = []

        self.dfs(0, -1, vis, adj, tin, low, bridges)
        return bridges
