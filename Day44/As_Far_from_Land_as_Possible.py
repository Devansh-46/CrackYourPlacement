class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        n, land, stack= len(grid), 0, []

        for i in range(n):
            for j in range(n):
                if grid[i][j]:
                    land+= 1
                    stack.append((i, j, 0))

        if land== n* n or not stack: return -1

        for i, j, distance in stack:
            for x, y in ((i, j+ 1), (i, j- 1), (i+ 1, j), (i- 1, j)):
                if 0<= x< n and 0<= y< n and grid[x][y]== 0:
                    grid[x][y]= 1
                    stack.append((x, y, distance+ 1))
        
        return stack[-1][-1]
