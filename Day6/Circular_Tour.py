class Solution:
    
    #Function to find starting point where the truck can start to get through
    #the complete circle without exhausting its petrol in between.
    def tour(self,lis, n):
        
        if n==1:
            return 0
            
        #considering first petrol pump as a starting point.
        start = 0
        end = 1
        cur_pos = lis[start][0] - lis[start][1]
        
        #we run a loop while all petrol pumps are not visited and we have 
        #reached first petrol pump again with 0 or more petrol.
        while(end != start or cur_pos < 0):
            
            #if current amount of petrol in truck becomes less than 0,
            #then remove the starting petrol pump from tour.
            while(cur_pos < 0 and start != end):
                
                #removing starting petrol pump and changing starting point.
                cur_pos -= (lis[start][0] - lis[start][1])
                start=(start+1)%n
                
                #if 0 is being considered as start again, then there 
                #is no possible solution.
                if start==0:
                    return -1
                    
            #adding a petrol pump to current tour.
            cur_pos+=(lis[end][0] - lis[end][1])
            end=(end+1)%n
            
        #returning starting point.
        return start
