# Back-end complete function Template for Python 3

# Function to count the number of nodes in the binary tree
def countNodes(n):
    # Base case: if node is None, return 0
    if n is None:
        return 0
    # Counting the current node and recursively counting the nodes in the left and right subtrees
    return 1 + countNodes(n.left) + countNodes(n.right)

# Function to find the target node and its value in the binary tree
def find(n, serialNo, target):
    # Base case: if node is None, return the current serial number and 0 as value
    if n is None:
        return (serialNo,0)
    
    # Recursively finding the target node in the left subtree
    # and updating the serial number and value
    serialNo, val = find(n.left, serialNo, target)
    
    # Incrementing the serial number
    serialNo+=1
    
    # If the serial number exceeds the target, return the current serial number and value
    if serialNo>target:
        return (serialNo,val)
    
    # If the serial number is equal to the target, return the current serial number and the node's value
    if serialNo==target:
        return (serialNo,n.data)
    
    # Recursively finding the target node in the right subtree
    # and updating the serial number and value
    return find(n.right, serialNo, target)

# Function to find the median of the binary tree
def findMedian(root):
    # Counting the total number of nodes in the tree
    n = countNodes(root)
    
    # If the total number of nodes is odd, finding the value of the middle node
    if n%2 == 1:
        return find( root, 0, 1+n//2 )[ 1 ]
    
    # If the total number of nodes is even, finding the values of the middle two nodes
    else:
        # Finding the values of the two middle nodes
        median = find( root, 0, n//2 )[ 1 ] + find( root, 0, 1+n//2 )[ 1 ]
        # Returning the median by dividing the sum by 2
        if median % 2:
            return median/2
        else:
            return median//2
