#Back-end complete function Template for Python 3

def pathToNode(root, path, k): 
  
    # base case handling 
    if root is None: 
        return False
  
     # append the node value in path 
    path.append(root.data) 
   
    # See if the k is same as root's data 
    if root.data == k : 
        return True
   
    # Check if k is found in left or right  
    # sub-tree 
    if ((root.left != None and pathToNode(root.left, path, k)) or
            (root.right!= None and pathToNode(root.right, path, k))): 
        return True
   
    # If not present in subtree rooted with root,  
    # remove root from path and return False  
    path.pop() 
    return False

class Solution:  
    def findDist(self,root, a, b): 
        if root: 
            # store path corresponding to node: a 
            path1 = [] 
            pathToNode(root, path1, a) 
  
            # store path corresponding to node: b 
            path2 = [] 
            pathToNode(root, path2, b) 
  
            # iterate through the paths to find the  
            # common path length 
            i=0
            while i<len(path1) and i<len(path2): 
                # get out as soon as the path differs  
                # or any path's length get exhausted 
                if path1[i] != path2[i]: 
                    break
                i = i+1
    
            # get the path length by deducting the  
            # intersecting path length (or till LCA) 
            return (len(path1)+len(path2)-2*i) 
        else: 
            return 0
