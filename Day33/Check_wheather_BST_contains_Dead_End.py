import sys
sys.setrecursionlimit(10**6)

class Solution:

    def getNodes(self, root, all, leaf):
        # Function to get all nodes and leaf nodes
        if root is None:
            return
        all.add(root.data)
        if(root.left is None and root.right is None):
            leaf.add(root.data)
            return
        self.getNodes(root.left, all, leaf)
        self.getNodes(root.right, all, leaf)
    
    def isDeadEnd(self, root):
        # Function to check if there is a dead end in the tree
        if root is None:
            return
        all = set()
        leaf = set()
        all.add(0)
        self.getNodes(root, all, leaf)
        for i in leaf:
            # Checking if there is a dead end
            if((i+1) in all and (i-1) in all):
                return True
        return False
        
