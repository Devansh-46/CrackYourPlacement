# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minCameraCover(self, root):
        result = [0]
        
        # 0 indicates that it doesn't need cam which might be a leaf node or a parent node which is already covered
        # < 3 indicates that it has already covered
        # >= 3 indicates that it needs a cam
        
        def getResult(root):
            if not root:
                return 0
            needsCam = getResult(root.left) + getResult(root.right)
            
            if needsCam == 0:
                return 3
            if needsCam < 3:
                return 0
            result[0]+=1
            return 1
         
        return result[0] + 1 if getResult(root) >= 3 else result[0]
