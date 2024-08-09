# Function to copy value of Node a to Node b
def copy_node(a, b):
    a.key = b.key
    a.left = b.left
    a.right = b.right

class Solution:
   def findPreSuc(self, root, pre, suc, key):

        while root:
            if root.key == key:
                if root.left:
                    tmp = root.left
                    while tmp.right:
                        tmp = tmp.right
                    copy_node(pre,tmp)

                if root.right:
                    tmp = root.right
                    while tmp.left:
                        tmp = tmp.left
                    copy_node(suc, tmp)

                return pre, suc

            if root.key > key:
                copy_node(suc, root)
                root = root.left
            else:
                copy_node(pre, root)
                root = root.right
                
