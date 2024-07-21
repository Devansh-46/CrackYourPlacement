#Back-end complete function Template for Python 3

class Solution:
    
    #Function to find if there is a celebrity in the party or not.
    def celebrity(self, M, n):
        
        #initializing two pointers for two corners.
        a = 0
        b = n-1
        
        #we keep moving till the a<b.
        while(a<b):
            if(M[a][b] == 1):
                a += 1
            else:
                b -= 1
                
        #checking if a is actually a celebrity or not.
        for i in range (n):
            
            #if any person doesn't know a or a knows any person, we return -1.
            if((i != a) and (M[a][i]==1 or M[i][a] == 0)):
                return -1;
                
        #if we reach here a is celebrity so we return a.
        return a
