class Solution(object):
    def floodFill(self, image, sr, sc, newColor):

        visit = set()
        ROWS, COLS = len(image), len(image[0])
        
        
        def isValid(r, c, prevVal):
            return False if r < 0 or c < 0 or r >= ROWS or c >= COLS or (r, c) in visit or image[r][c] != prevVal else True
        
        
        def dfs(r, c, prevVal):
            if not isValid(r, c, prevVal):
                return
            visit.add((r, c))
            temp = image[r][c]
            image[r][c] = newColor
            dfs(r+1, c, temp)
            dfs(r-1, c, temp)
            dfs(r, c+1, temp)
            dfs(r, c-1, temp)
            
        
        
        dfs(sr, sc, image[sr][sc])
        return image