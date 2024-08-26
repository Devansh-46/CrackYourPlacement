#Back-end complete function Template for Python 3

def constructTree(pre, preLN, n): 
    index = [0] 
    return constructTreeUtil(pre, preLN, index, n) 

def constructTreeUtil(pre, preLN, index_ptr, n): 
      
    index = index_ptr[0] # store the current value  
                         # of index in pre[]  
    if index == n:  
        return None
  
    temp = Node(pre[index])  
    index_ptr[0] += 1
  
   
    if preLN[index] == 'N': 
        temp.left = constructTreeUtil(pre, preLN,  
                                      index_ptr, n)  
        temp.right = constructTreeUtil(pre, preLN,  
                                       index_ptr, n)  
  
    return temp
