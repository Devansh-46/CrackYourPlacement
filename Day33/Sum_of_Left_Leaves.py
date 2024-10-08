# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def dfs(node, isLeft):
            if node:
                if isLeft and not node.left and not node.right:
                    return node.val

                return dfs(node.left, True) + dfs(node.right, False)

            return 0
        
        return dfs(root, False)
