class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        ones, zeros = 0, 0
        m, n = len(grid), len(grid[0])
        # Count for number of lands present in the grid
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    ones += 1
                else:
                    zeros += 1
        # If no lands are present, max size will be 1
        if ones == 0:
            return 1
        # If no water is present, max size will be the whole grid
        if zeros == 0:
            return ones
        # get count of islands and each island size
        islandSize = dict()
        islandNum = 1
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        # Complexity - O(n^2)
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    # Perform BFS and assign a island number to each land part of the same island
                    islandNum += 1
                    grid[i][j] = islandNum
                    queue = [(i, j)]
                    count = 1
                    while queue:
                        r, c = queue.pop(0)
                        for nbr in directions:
                            nr, nc = r + nbr[0], c + nbr[1]
                            if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == 1:
                                grid[nr][nc] = islandNum
                                # Increase the count of lands present in the island
                                count += 1
                                queue.append((nr, nc))
                    # For each island number, assign the size of the island
                    islandSize[islandNum] = count
        # iterate over water and check if any islands are surrounding that island cell
        # If distinct islands are surrounding the water, add the size of distinct islands and add 1
        # corresponding to water converted to land
        # Complexity - O(n^2)
        largestIsland = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    size = 1
                    distinctIslands = set()
                    for nbr in directions:
                        nr, nc = i + nbr[0], j + nbr[1]
                        if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] != 0:
                            distinctIslands.add(grid[nr][nc])
                    for d in distinctIslands:
                        size += islandSize[d]
                    largestIsland = max(largestIsland, size)
        # print(islandSize)
        # print(grid)
        return largestIsland
