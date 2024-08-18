# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def count_paths_from_node(node: Optional[TreeNode], target: int) -> int:
            if not node:
                return 0
            
            # Check the current node path and its children
            count = 0
            if node.val == target:
                count += 1
            
            count += count_paths_from_node(node.left, target - node.val)
            count += count_paths_from_node(node.right, target - node.val)
            
            return count

        def dfs(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            
            # Count paths that start from the current node
            count = count_paths_from_node(node, targetSum)
            
            # Recur on left and right subtree
            count += dfs(node.left)
            count += dfs(node.right)
            
            return count

        # Start DFS from the root
        return dfs(root)
