class Solution:
    
    def getCount(self,root,low,high):
        
        if root == None: 
            return 0
              
        #if data at current node is equal to lower and upper range, we return 1.
        if root.data == high and root.data == low:  
            return 1
      
        if root.data <= high and root.data >= low:  
            return (1+self.getCount(root.left,low,high)+self.getCount(root.right,low,high)) 
      
        elif root.data < low:  
            return self.getCount(root.right, low, high) 
      
        else: 
            return self.getCount(root.left, low, high) 
     
