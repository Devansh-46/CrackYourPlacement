# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        plus = root.val
        bfs = deque([(root,plus)])
        while bfs:
            node,curr_sum = bfs.popleft()
            if (not node.left and not node.right) and curr_sum == targetSum:
                return True
            if node.left and node.right:
                curr_sum+=node.left.val
                bfs.append((node.left,curr_sum))
                curr_sum = curr_sum - node.left.val + node.right.val
                bfs.append((node.right,curr_sum))
            elif node.left:
                curr_sum+=node.left.val
                bfs.append((node.left,curr_sum))
            elif node.right:
                curr_sum+=node.right.val
                bfs.append((node.right,curr_sum))
        return False
        
