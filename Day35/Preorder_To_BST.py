class Node:

    def __init__(self, data=0):
        self.data = data
        self.left = None
        self.right = None


#Function that constructs BST from its preorder traversal.
def Bst(pre, size):

    #first element of preorder traversal is always root of BST.
    root = Node(pre[0])

    #creating a stack of capacity equal to size of array.
    s = []
    #pushing root into the stack.
    s.append(root)

    i = 1
    #iterating over rest of the array elements.
    while (i < size):

        temp = None

        #we keep on popping from stack while data at top of stack is less
        #than the current array element.
        while (len(s) > 0 and pre[i] > s[-1].data):
            temp = s.pop()

        #we make this greater value as the right child and push it into stack.
        if (temp != None):
            temp.right = Node(pre[i])
            s.append(temp.right)

        #if current array element is less than data at top of stack, we make
        #it as the left child of the stack's top node and push it into stack.
        else:
            temp = s[-1]
            temp.left = Node(pre[i])
            s.append(temp.left)
        i = i + 1

    return root
