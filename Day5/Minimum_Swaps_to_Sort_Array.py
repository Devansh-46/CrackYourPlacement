class Solution:
    
    #Function to find the minimum number of swaps required to sort the array.
    def minSwaps(self, nums):
        
        n = len(nums)
        cur = []
        
        #iterating over the array elements.
        for i in range(n):
            
            #storing the elements and their position as pair in the list.
            cur.append([nums[i], i])
            
        #sorting the list.
        cur.sort()
        
        #using boolean list to mark visited elements and currently 
        #marking all the nodes as false.
        vis = [False for i in range(n)]
        ans = 0
        for i in range(n):
            
            #if element is already visited or it is already at
		    #correct position, we continue the loop.
            if(vis[i] or cur[i][1] == i):
                continue
            else:
                cycle_size = 0
                j = i
                
                #while element is not visited, we find out the number of nodes 
                #in this cycle and keep incrementing cycle size.
                while(vis[j] == False):
                    vis[j] = True
                    j = cur[j][1]
                    cycle_size = cycle_size + 1
                    
                #updating number of swaps required.
                ans = ans + max(0, cycle_size - 1)
                
        return ans
