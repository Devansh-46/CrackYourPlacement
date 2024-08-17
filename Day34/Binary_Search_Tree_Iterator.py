# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:
    st=[]
    def __init__(self, root: Optional[TreeNode]):
        def inorder(root):
            if root is None:
                return
            inorder(root.left)
            self.st.append(root.val)
            inorder(root.right)
        inorder(root)
    def next(self) -> int:
        return self.st.pop(0)
    def hasNext(self) -> bool:
        return len(self.st)>0


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
