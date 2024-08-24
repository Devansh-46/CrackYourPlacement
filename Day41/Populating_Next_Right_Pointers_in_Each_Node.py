"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        dict1 = {}
    
        def dfs(node, level):
            if not node:
                return
        
            dfs(node.left, level+1)
            dfs(node.right, level+1)
    
            if level in dict1:
                dict1[level].next = node
                dict1[level] = node
            else:
                dict1[level] = node
    
        dfs(root,0)
            
        return root
