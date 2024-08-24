#User function Template for python3

'''
class Node:
    """ Class Node """
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None
'''

def fixPrevPtr(root):
    if root is not None:
        fixPrevPtr(root.left)
        root.left = fixPrevPtr.pre
        fixPrevPtr.pre = root
        fixPrevPtr(root.right)


def fixNextPtr(root):
    
    prev = None
    while (root and root.right != None):
        root = root.right
     
    while (root and root.left != None):
        prev = root
        root = root.left
        root.right = prev
        
    return root


class Solution:
    def bToDLL(self,root):
        fixPrevPtr.pre = None
        fixPrevPtr(root)
        return fixNextPtr(root)

