class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        dist = [[float("inf")] * n for i in range(n)]
        dist[0][0] = grid[0][0]
        pq = [(grid[0][0], 0, 0)]
        moves = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        while pq:
            w, i, j = heappop(pq)
            if (i, j) == (n - 1, n - 1):
                return w
            for move in moves:
                y, x = i + move[0], j + move[1]
                if y < 0 or y >= n or x < 0 or x >= n:
                    continue
                if max(w, grid[y][x]) < dist[y][x]:
                    dist[y][x] = max(w, grid[y][x])
                    heappush(pq, (dist[y][x], y, x))
        
