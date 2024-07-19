class Solution:
    #Function to find minimum time required to rot all oranges. 
    def orangesRotting(self, grid):
        from queue import Queue
        
        
        ct = 0 
        res = -1 
        
        #queue to store cells which have rotten oranges.
        q = Queue()
        dx = [-1,1,0,0]
        dy = [0,0,-1,1]
        
        #traversing over all the cells of the matrix.
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                
                #if grid value is more than 0, we increment the counter.
                if grid[i][j]>0:
                    ct+=1
                    
                #if grid value is 2, we push the cell indexes into queue.
                if(grid[i][j]==2):
                    q.put([i,j])
        
        while not q.empty():
            
            #incrementing result counter.
            res+=1 
            size = q.qsize()
            for k in range(size):
                
                #popping the front element of queue and storing cell indexes.
                cur = q.get()
                ct -= 1
                
                #traversing the adjacent vertices.
                for i in range(4):
                    x = cur[0] + dx[i]
                    y = cur[1] + dy[i]
                    
                    #if cell indexes are within matrix bounds and grid value
                    #is not 1, we continue the loop else we store 2 in current
                    #cell and push the cell indexes in the queue.
                    if x>=len(grid) or x<0 or y>=len(grid[0]) or y<0 or grid[x][y]!=1:
                        continue
                    grid[x][y] = 2
                    q.put([x,y])
        
        #returning the minimum time.
        if ct:
            return -1
        else:
            return max(0,res)
            
            
            
